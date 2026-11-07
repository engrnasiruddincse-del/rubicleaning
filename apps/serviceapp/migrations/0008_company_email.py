from django.db import migrations


def set_email(apps, schema_editor):
    MyCompany = apps.get_model("serviceapp", "MyCompany")
    MyCompany.objects.filter(email__isnull=True).update(email="servicesrubicleaning@gmail.com")
    MyCompany.objects.filter(email="").update(email="servicesrubicleaning@gmail.com")


class Migration(migrations.Migration):

    dependencies = [
        ("serviceapp", "0007_work_examples"),
    ]

    operations = [
        migrations.RunPython(set_email, migrations.RunPython.noop),
    ]
