"""Compile locale/*/LC_MESSAGES/django.po to .mo without GNU gettext (works on Windows).

Usage: python manage.py build_translations
"""
import ast
import struct
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand


def parse_po(path):
    messages, msgid, msgstr, section = {}, None, None, None

    def flush():
        if msgid is not None and msgstr:
            messages[msgid] = msgstr

    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("msgid "):
            flush()
            msgid, msgstr, section = ast.literal_eval(line[6:]), None, "id"
        elif line.startswith("msgstr "):
            msgstr, section = ast.literal_eval(line[7:]), "str"
        elif line.startswith('"'):
            if section == "id":
                msgid += ast.literal_eval(line)
            elif section == "str":
                msgstr += ast.literal_eval(line)
    flush()
    return messages


def write_mo(messages, path):
    keys = sorted(messages)
    ids = [k.encode("utf-8") for k in keys]
    strs = [messages[k].encode("utf-8") for k in keys]
    header_size = 7 * 4
    table_size = len(keys) * 8
    id_start = header_size + 2 * table_size
    str_start = id_start + sum(len(i) + 1 for i in ids)

    id_table, str_table, offset = [], [], id_start
    for i in ids:
        id_table += [len(i), offset]
        offset += len(i) + 1
    offset = str_start
    for s in strs:
        str_table += [len(s), offset]
        offset += len(s) + 1

    out = struct.pack("Iiiiiii", 0x950412DE, 0, len(keys), header_size,
                      header_size + table_size, 0, 0)
    out += struct.pack(f"{len(id_table)}i", *id_table)
    out += struct.pack(f"{len(str_table)}i", *str_table)
    out += b"".join(i + b"\0" for i in ids)
    out += b"".join(s + b"\0" for s in strs)
    Path(path).write_bytes(out)


class Command(BaseCommand):
    help = "Compile .po translation files to .mo using pure Python."

    def handle(self, *args, **options):
        for locale_dir in settings.LOCALE_PATHS:
            for po in Path(locale_dir).glob("*/LC_MESSAGES/*.po"):
                messages = parse_po(po)
                write_mo(messages, po.with_suffix(".mo"))
                self.stdout.write(f"{po} -> {po.with_suffix('.mo').name} ({len(messages)} messages)")
