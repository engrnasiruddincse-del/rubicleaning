from django.db import migrations


COMPANY = {
    "name": "Rubi Cleaning",
    "slug": "rubi-cleaning",
    "address": "Majaka tn 23, 11416 Tallinn, Estonia",
    "phone": "+372 5324 6598",
    "website": "https://rubicleaning.ee",
}

SERVICES_ET = {
    "regular-cleaning": (
        "Tavakoristus",
        "<p>Hoidke oma kodu nädalast nädalasse värske ja puhas – kõigi tubade regulaarne koristus. "
        "Sobib igas suuruses korteritele ja majadele.</p>"
        "<ul><li>Pindade, riiulite ja põrandaliistude tolmuvabaks tegemine</li>"
        "<li>Kõigi põrandate tolmuimemine ja pesemine</li>"
        "<li>Köögipindade, valamu ja seadmete välispindade puhastus</li>"
        "<li>Vannitoa ja WC puhastus</li>"
        "<li>Prügikastide tühjendamine ja korrastamine</li></ul>",
    ),
    "deep-cleaning": (
        "Suurpuhastus",
        "<p>Põhjalik koristus ülevalt alla kodudele, mis vajavad tavapärasest rohkem: "
        "rasv, katlakivi ja raskesti märgatavad kohad.</p>"
        "<ul><li>Kõik tavakoristuse tööd, põhjalikumalt</li>"
        "<li>Ahju, külmkapi ja mikrolaineahju puhastus seest</li>"
        "<li>Katlakivi eemaldamine kraanidelt, plaatidelt ja dušiseintelt</li>"
        "<li>Uksed, uksepiidad, lülitid ja radiaatorid</li>"
        "<li>Liigutatava mööbli tagant ja alt</li></ul>",
    ),
    "after-renovation-cleaning": (
        "Remondijärgne koristus",
        "<p>Eemaldame ehitustolmu, värviplekid ja prahi pärast ehitus- või remonditöid, "
        "et saaksite kohe sisse kolida.</p>"
        "<ul><li>Peene tolmu eemaldamine kõikidelt pindadelt</li>"
        "<li>Värvi-, krohvi- ja liimiplekkide eemaldamine</li>"
        "<li>Akende, raamide ja aknalaudade puhastus</li>"
        "<li>Põrandate tolmuimemine ja pesemine</li>"
        "<li>Köögi- ja vannitoasisustuse poleerimine</li></ul>",
    ),
    "move-in-move-out-cleaning": (
        "Kolimiskoristus",
        "<p>Tühja kinnisvara põhjalik koristus enne sissekolimist või pärast väljakolimist – "
        "valmis üleandmiseks omanikule või järgmisele üürnikule.</p>"
        "<ul><li>Kõikide kappide, riidekappide ja sahtlite sisemus</li>"
        "<li>Köögiseadmed seest ja väljast</li>"
        "<li>Vannitubade katlakivi eemaldus ja desinfitseerimine</li>"
        "<li>Seinte plekkide eemaldus, põrandate pesu</li>"
        "<li>Akende ja rõdu puhastus soovi korral</li></ul>",
    ),
    "window-cleaning": (
        "Akende pesu",
        "<p>Triibuvabad aknad, mis lasevad valguse sisse – kasutame professionaalseid tööriistu "
        "ja ohutuid puhastusvahendeid.</p>"
        "<ul><li>Klaasid seest ja väljast</li>"
        "<li>Raamid, aknalauad ja liistud</li>"
        "<li>Rõduuksed ja klaasseinad</li>"
        "<li>Hind akna kohta – maksate ainult vajaliku eest</li></ul>",
    ),
    "sofa-cleaning": (
        "Diivani puhastus",
        "<p>Pehme mööbli süvapuhastus ja värskendamine – eemaldame plekid, lõhnad, "
        "tolmulestad ja allergeenid.</p>"
        "<ul><li>Diivanid, tugitoolid ja pehmed toolid</li>"
        "<li>Professionaalne ekstraktsioonpuhastus</li>"
        "<li>Plekkide ja lõhnade töötlemine</li>"
        "<li>Kangasõbralikud vahendid, kiire kuivamine</li></ul>",
    ),
    "snow-cleaning": (
        "Lumekoristus",
        "<p>Kiire ja usaldusväärne lume- ja jääkoristus, et teie pere ja kliendid pääseksid "
        "kogu talve turvaliselt liikuma.</p>"
        "<ul><li>Sissesõiduteede, kõnniteede ja sissepääsude puhastus</li>"
        "<li>Trepid, verandad ja parkimiskohad</li>"
        "<li>Jäätõrje libisemise vältimiseks</li>"
        "<li>Ühekordsed väljakutsed või hooajalepingud kodudele ja ettevõtetele</li></ul>",
    ),
}

# Starting prices: nztcleaning.ee rates minus €2–4. Snow cleaning has no reference price.
PRICING = [
    ("Regular Cleaning", "Tavakoristus", "€35",
     ["One-room apartment", "Kitchen, bathroom and floors", "Cleaning supplies included"],
     ["Ühetoaline korter", "Köök, vannituba ja põrandad", "Puhastusvahendid hinna sees"]),
    ("Deep Cleaning", "Suurpuhastus", "€95",
     ["Oven, fridge and limescale", "Behind furniture and high surfaces", "Ideal before guests or seasonally"],
     ["Ahi, külmkapp ja katlakivi", "Mööbli tagant ja kõrgetelt pindadelt", "Ideaalne enne külalisi või hooajaliselt"]),
    ("After Renovation Cleaning", "Remondijärgne koristus", "€125",
     ["Construction dust removal", "Paint and plaster spots", "Windows and frames included"],
     ["Ehitustolmu eemaldus", "Värvi- ja krohviplekid", "Aknad ja raamid hinna sees"]),
    ("Move In / Move Out Cleaning", "Kolimiskoristus", "€105",
     ["Inside cupboards and appliances", "Ready for handover to owner or tenant", "Empty property"],
     ["Kappide ja seadmete sisemus", "Valmis üleandmiseks omanikule või üürnikule", "Tühi kinnisvara"]),
    ("Window Cleaning", "Akende pesu", "€5",
     ["Price per window", "Glass inside and out", "Frames and sills wiped"],
     ["Hind akna kohta", "Klaasid seest ja väljast", "Raamid ja aknalauad puhtaks"]),
    ("Sofa Cleaning", "Diivani puhastus", "€55",
     ["Sofas and armchairs", "Stain and odour treatment", "Quick drying"],
     ["Diivanid ja tugitoolid", "Plekkide ja lõhnade töötlus", "Kiire kuivamine"]),
    ("Snow Cleaning", "Lumekoristus", "€45",
     ["Driveways and footpaths", "Ice treatment against slipping", "One-off or seasonal plans"],
     ["Sissesõiduteed ja kõnniteed", "Jäätõrje libisemise vastu", "Ühekordne või hooajaleping"]),
]

LOCATIONS = [
    ("Kesklinn", "City centre, Old Town and Kadriorg", "Kesklinn, vanalinn ja Kadriorg"),
    ("Põhja-Tallinn", "Kalamaja, Pelgulinn and Kopli", "Kalamaja, Pelgulinn ja Kopli"),
    ("Lasnamäe", "Tallinn's largest residential district", "Tallinna suurim elurajoon"),
    ("Mustamäe / Kristiine", "Including Haabersti and Õismäe", "Sealhulgas Haabersti ja Õismäe"),
    ("Pirita / Nõmme", "Green residential areas", "Rohelised elurajoonid"),
    ("Harjumaa", "Viimsi, Saue, Rae and more by request", "Viimsi, Saue, Rae jt kokkuleppel"),
]

FAQS = [
    ("Do I need to provide cleaning supplies?",
     "Kas pean ise puhastusvahendid andma?",
     "No. Our cleaners bring all the products and equipment they need.",
     "Ei. Meie koristajad toovad kõik vajalikud vahendid ja seadmed kaasa."),
    ("How do I book a cleaning?",
     "Kuidas koristust broneerida?",
     "Fill in the quote form, call us or message us on WhatsApp. We'll confirm a time that suits you.",
     "Täitke hinnapäringu vorm, helistage või kirjutage meile WhatsAppis. Lepime kokku teile sobiva aja."),
    ("Are the prices on the website final?",
     "Kas kodulehel toodud hinnad on lõplikud?",
     "They are starting prices. The final price depends on the size and condition of the space, "
     "and we confirm it with you before we start.",
     "Need on alghinnad. Lõplik hind sõltub pinna suurusest ja seisukorrast ning lepime selle "
     "teiega kokku enne töö algust."),
    ("Do you offer snow cleaning all winter?",
     "Kas pakute lumekoristust kogu talve?",
     "Yes. You can book a one-off visit after a snowfall or a seasonal plan for your home or business.",
     "Jah. Võite tellida ühekordse väljakutse pärast lumesadu või hooajalepingu oma kodule või ettevõttele."),
]


def seed(apps, schema_editor):
    MyCompany = apps.get_model("serviceapp", "MyCompany")
    Service = apps.get_model("serviceapp", "Service")
    Pricing = apps.get_model("serviceapp", "Pricing")
    ServiceLocation = apps.get_model("serviceapp", "ServiceLocation")
    FAQ = apps.get_model("serviceapp", "FAQ")

    company = MyCompany.objects.first()
    if company is None:
        MyCompany.objects.create(**COMPANY)
    else:
        for key, value in COMPANY.items():
            setattr(company, key, value)
        company.save()

    for slug, (name_et, description_et) in SERVICES_ET.items():
        Service.objects.filter(slug=slug).update(name_et=name_et, description_et=description_et)

    if not Pricing.objects.exists():
        for order, (title, title_et, price, features, features_et) in enumerate(PRICING):
            Pricing.objects.create(
                title=title, title_et=title_et, price=price,
                features="\n".join(features), features_et="\n".join(features_et),
                button_text="Book Now", button_text_et="Broneeri", order=order,
            )

    if not ServiceLocation.objects.exists():
        for name, description, description_et in LOCATIONS:
            ServiceLocation.objects.create(name=name, description=description, description_et=description_et)

    if not FAQ.objects.filter(is_general=True).exists():
        for question, question_et, answer, answer_et in FAQS:
            FAQ.objects.create(
                question=question, question_et=question_et,
                answer=answer, answer_et=answer_et, is_general=True,
            )


class Migration(migrations.Migration):

    dependencies = [
        ("serviceapp", "0005_estonian_fields"),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
