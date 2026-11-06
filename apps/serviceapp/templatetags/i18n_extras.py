from django import template

from ..models import localized

register = template.Library()


@register.filter
def loc(obj, field):
    """{{ service|loc:"name" }} -> Estonian value when active language is et, else English."""
    return localized(obj, field)


@register.filter
def service_image(service):
    """Uploaded image if any, else static/assets/services/<slug>.jpg if it exists, else ''."""
    from django.contrib.staticfiles import finders
    from django.templatetags.static import static

    if service.image:
        return service.image.url
    path = f"assets/services/{service.slug}.jpg"
    return static(path) if finders.find(path) else ""


@register.simple_tag
def whatsapp_book_url(company, service_name, price=""):
    """wa.me link with a pre-filled booking message for one service, in the active language."""
    from urllib.parse import quote

    from django.urls import reverse
    from django.utils.translation import gettext as _

    phone = "".join(ch for ch in (getattr(company, "phone", "") or "") if ch.isdigit())
    if not phone:
        return reverse("home") + "#quote"
    if price:
        text = _("Hello! I would like to book: %(service)s (from %(price)s).") % {"service": service_name, "price": price}
    else:
        text = _("Hello! I would like to book: %(service)s.") % {"service": service_name}
    text += "\n" + _("Address:") + "\n" + _("Preferred date and time:")
    return f"https://wa.me/{phone}?text={quote(text)}"
