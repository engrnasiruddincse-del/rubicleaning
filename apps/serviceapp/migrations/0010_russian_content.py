from django.db import migrations


SERVICES_RU = {
    "regular-cleaning": (
        "Регулярная уборка",
        "<p>Поддерживайте дом свежим и чистым неделю за неделей — регулярная уборка всех комнат. "
        "Подходит для квартир и домов любого размера.</p>"
        "<ul><li>Удаление пыли с поверхностей, полок и плинтусов</li>"
        "<li>Пылесос и мытьё всех полов</li>"
        "<li>Протирка кухонных поверхностей, мойки и техники снаружи</li>"
        "<li>Уборка ванной комнаты и туалета</li>"
        "<li>Вынос мусора и наведение порядка</li></ul>",
    ),
    "deep-cleaning": (
        "Генеральная уборка",
        "<p>Тщательная уборка сверху донизу для домов, которым нужно больше, чем обычная уборка: "
        "жир, известковый налёт и труднодоступные места.</p>"
        "<ul><li>Всё, что входит в регулярную уборку, но более детально</li>"
        "<li>Чистка духовки, холодильника и микроволновки внутри</li>"
        "<li>Удаление налёта с кранов, плитки и душевых стенок</li>"
        "<li>Двери, дверные коробки, выключатели и радиаторы</li>"
        "<li>За и под передвигаемой мебелью</li></ul>",
    ),
    "after-renovation-cleaning": (
        "Уборка после ремонта",
        "<p>Удаляем строительную пыль, следы краски и мусор после строительных или ремонтных работ, "
        "чтобы вы могли сразу заселиться.</p>"
        "<ul><li>Удаление мелкой пыли со всех поверхностей</li>"
        "<li>Удаление пятен краски, штукатурки и клея</li>"
        "<li>Мытьё окон, рам и подоконников</li>"
        "<li>Пылесос и мытьё полов</li>"
        "<li>Полировка сантехники и кухонной фурнитуры</li></ul>",
    ),
    "move-in-move-out-cleaning": (
        "Уборка при переезде",
        "<p>Тщательная уборка пустой квартиры перед заселением или после выезда — "
        "готово к передаче владельцу или следующему арендатору.</p>"
        "<ul><li>Внутри всех шкафов, гардеробов и ящиков</li>"
        "<li>Кухонная техника внутри и снаружи</li>"
        "<li>Удаление налёта и дезинфекция ванных комнат</li>"
        "<li>Удаление пятен со стен, мытьё полов</li>"
        "<li>Мытьё окон и балкона по желанию</li></ul>",
    ),
    "window-cleaning": (
        "Мытьё окон",
        "<p>Окна без разводов, которые пропускают свет, — профессиональные инструменты "
        "и безопасные средства.</p>"
        "<ul><li>Стёкла изнутри и снаружи</li>"
        "<li>Рамы, подоконники и направляющие</li>"
        "<li>Балконные двери и стеклянные перегородки</li>"
        "<li>Цена за окно — вы платите только за нужное</li></ul>",
    ),
    "sofa-cleaning": (
        "Чистка дивана",
        "<p>Глубокая чистка и освежение мягкой мебели — удаляем пятна, запахи, "
        "пылевых клещей и аллергены.</p>"
        "<ul><li>Диваны, кресла и мягкие стулья</li>"
        "<li>Профессиональная экстракторная чистка</li>"
        "<li>Обработка пятен и запахов</li>"
        "<li>Бережные к ткани средства, быстрое высыхание</li></ul>",
    ),
    "snow-cleaning": (
        "Уборка снега",
        "<p>Быстрая и надёжная уборка снега и льда, чтобы ваша семья и клиенты "
        "всю зиму могли безопасно передвигаться.</p>"
        "<ul><li>Очистка подъездных дорожек, тротуаров и входов</li>"
        "<li>Ступени, крыльцо и парковочные места</li>"
        "<li>Обработка от гололёда</li>"
        "<li>Разовые выезды или сезонные договоры для домов и компаний</li></ul>",
    ),
}

# Pricing rows are matched by their English title (same as the service name).
PRICING_RU = {
    "Regular Cleaning": ["Однокомнатная квартира", "Кухня, ванная и полы", "Чистящие средства включены"],
    "Deep Cleaning": ["Духовка, холодильник и налёт", "За мебелью и на высоких поверхностях", "Идеально перед приездом гостей или по сезону"],
    "After Renovation Cleaning": ["Удаление строительной пыли", "Пятна краски и штукатурки", "Окна и рамы включены"],
    "Move In / Move Out Cleaning": ["Внутри шкафов и техники", "Готово к передаче владельцу или арендатору", "Пустая квартира"],
    "Window Cleaning": ["Цена за одно окно", "Стёкла изнутри и снаружи", "Протирка рам и подоконников"],
    "Sofa Cleaning": ["Диваны и кресла", "Обработка пятен и запахов", "Быстрое высыхание"],
    "Snow Cleaning": ["Подъездные дорожки и тротуары", "Обработка от гололёда", "Разовый выезд или сезонный договор"],
}
SERVICE_SLUG_BY_TITLE = {
    "Regular Cleaning": "regular-cleaning",
    "Deep Cleaning": "deep-cleaning",
    "After Renovation Cleaning": "after-renovation-cleaning",
    "Move In / Move Out Cleaning": "move-in-move-out-cleaning",
    "Window Cleaning": "window-cleaning",
    "Sofa Cleaning": "sofa-cleaning",
    "Snow Cleaning": "snow-cleaning",
}

LOCATIONS_RU = {
    "Kesklinn": "Центр, Старый город и Кадриорг",
    "Põhja-Tallinn": "Каламая, Пельгулинн и Копли",
    "Lasnamäe": "Крупнейший жилой район Таллинна",
    "Mustamäe / Kristiine": "Включая Хааберсти и Ыйсмяэ",
    "Pirita / Nõmme": "Зелёные жилые районы",
    "Harjumaa": "Виймси, Сауэ, Раэ и др. по договорённости",
}

FAQS_RU = {
    "Do I need to provide cleaning supplies?": (
        "Нужно ли мне предоставлять чистящие средства?",
        "Нет. Наши уборщики привозят все необходимые средства и оборудование.",
    ),
    "How do I book a cleaning?": (
        "Как заказать уборку?",
        "Заполните форму запроса, позвоните нам или напишите в WhatsApp. Мы согласуем удобное для вас время.",
    ),
    "Are the prices on the website final?": (
        "Окончательны ли цены на сайте?",
        "Это начальные цены. Окончательная цена зависит от площади и состояния помещения, "
        "и мы согласуем её с вами до начала работы.",
    ),
    "Do you offer snow cleaning all winter?": (
        "Предлагаете ли вы уборку снега всю зиму?",
        "Да. Можно заказать разовый выезд после снегопада или сезонный договор для дома или компании.",
    ),
}


def seed(apps, schema_editor):
    Service = apps.get_model("serviceapp", "Service")
    Pricing = apps.get_model("serviceapp", "Pricing")
    ServiceLocation = apps.get_model("serviceapp", "ServiceLocation")
    FAQ = apps.get_model("serviceapp", "FAQ")

    # Only fill empty fields, so edits made in admin are never overwritten.
    for slug, (name_ru, description_ru) in SERVICES_RU.items():
        Service.objects.filter(slug=slug, name_ru="").update(name_ru=name_ru)
        Service.objects.filter(slug=slug, description_ru="").update(description_ru=description_ru)

    for title, features in PRICING_RU.items():
        name_ru = SERVICES_RU[SERVICE_SLUG_BY_TITLE[title]][0]
        Pricing.objects.filter(title=title, title_ru="").update(title_ru=name_ru)
        Pricing.objects.filter(title=title, features_ru="").update(features_ru="\n".join(features))
        Pricing.objects.filter(title=title, button_text_ru="").update(button_text_ru="Забронировать")

    for name, description_ru in LOCATIONS_RU.items():
        ServiceLocation.objects.filter(name=name, description_ru="").update(description_ru=description_ru)

    for question, (question_ru, answer_ru) in FAQS_RU.items():
        FAQ.objects.filter(question=question, question_ru="").update(question_ru=question_ru)
        FAQ.objects.filter(question=question, answer_ru="").update(answer_ru=answer_ru)


class Migration(migrations.Migration):

    dependencies = [
        ("serviceapp", "0009_russian_fields"),
    ]

    operations = [
        migrations.RunPython(seed, migrations.RunPython.noop),
    ]
