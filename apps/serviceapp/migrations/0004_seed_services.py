from django.db import migrations


SERVICES = [
    {
        "slug": "regular-cleaning",
        "name": "Regular Cleaning",
        "is_popular": True,
        "description": (
            "<p>Keep your home fresh week after week with a routine clean of every room. "
            "Ideal for apartments and houses of any size.</p>"
            "<ul><li>Dusting of surfaces, shelves and skirting boards</li>"
            "<li>Vacuuming and mopping of all floors</li>"
            "<li>Kitchen wipe-down, sink and appliance exteriors</li>"
            "<li>Bathroom and toilet cleaning</li>"
            "<li>Emptying bins and tidying up</li></ul>"
        ),
    },
    {
        "slug": "deep-cleaning",
        "name": "Deep Cleaning",
        "is_popular": True,
        "description": (
            "<p>A top-to-bottom clean for homes that need more than the usual routine: "
            "built-up grease, limescale and the spots that are easy to miss.</p>"
            "<ul><li>Everything in a regular clean, in more detail</li>"
            "<li>Inside the oven, fridge and microwave</li>"
            "<li>Descaling of taps, tiles and shower screens</li>"
            "<li>Doors, door frames, switches and radiators</li>"
            "<li>Behind and under movable furniture</li></ul>"
        ),
    },
    {
        "slug": "after-renovation-cleaning",
        "name": "After Renovation Cleaning",
        "is_popular": False,
        "description": (
            "<p>We remove construction dust, paint marks and leftover debris after building or "
            "renovation work so your space is ready to live in.</p>"
            "<ul><li>Fine dust removal from every surface</li>"
            "<li>Paint, plaster and adhesive spot removal</li>"
            "<li>Cleaning of windows, frames and sills</li>"
            "<li>Floors vacuumed and washed</li>"
            "<li>Kitchen and bathroom fixtures polished</li></ul>"
        ),
    },
    {
        "slug": "move-in-move-out-cleaning",
        "name": "Move In / Move Out Cleaning",
        "is_popular": True,
        "description": (
            "<p>A thorough clean of an empty property before you move in or after you move out, "
            "ready for handover to the owner or next tenant.</p>"
            "<ul><li>Inside all cupboards, wardrobes and drawers</li>"
            "<li>Kitchen appliances inside and out</li>"
            "<li>Bathrooms descaled and disinfected</li>"
            "<li>Walls spot-cleaned, floors washed</li>"
            "<li>Windows and balcony cleaned on request</li></ul>"
        ),
    },
    {
        "slug": "window-cleaning",
        "name": "Window Cleaning",
        "is_popular": False,
        "description": (
            "<p>Streak-free windows that let the light in, using professional tools and "
            "safe cleaning products.</p>"
            "<ul><li>Glass cleaned inside and out</li>"
            "<li>Frames, sills and tracks wiped</li>"
            "<li>Balcony doors and glass partitions</li>"
            "<li>Priced per window, so you only pay for what you need</li></ul>"
        ),
    },
    {
        "slug": "sofa-cleaning",
        "name": "Sofa Cleaning",
        "is_popular": False,
        "description": (
            "<p>Deep cleaning and refreshing of upholstered furniture to remove stains, "
            "odours, dust mites and allergens.</p>"
            "<ul><li>Sofas, armchairs and upholstered chairs</li>"
            "<li>Professional extraction cleaning</li>"
            "<li>Stain and odour treatment</li>"
            "<li>Fabric-safe products, quick drying</li></ul>"
        ),
    },
    {
        "slug": "snow-cleaning",
        "name": "Snow Cleaning",
        "is_popular": True,
        "description": (
            "<p>Fast, reliable snow and ice removal so you, your family and your customers can "
            "get in and out safely all winter.</p>"
            "<ul><li>Driveways, footpaths and entrances cleared</li>"
            "<li>Steps, porches and parking spaces</li>"
            "<li>Ice treatment to prevent slips</li>"
            "<li>One-off visits or seasonal plans for homes and businesses</li></ul>"
        ),
    },
]


def seed_services(apps, schema_editor):
    Service = apps.get_model("serviceapp", "Service")
    for data in SERVICES:
        Service.objects.update_or_create(
            slug=data["slug"],
            defaults={
                "name": data["name"],
                "description": data["description"],
                "is_popular": data["is_popular"],
                "is_active": True,
            },
        )


def unseed_services(apps, schema_editor):
    Service = apps.get_model("serviceapp", "Service")
    Service.objects.filter(slug__in=[s["slug"] for s in SERVICES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("serviceapp", "0003_contact_is_read"),
    ]

    operations = [
        migrations.RunPython(seed_services, unseed_services),
    ]
