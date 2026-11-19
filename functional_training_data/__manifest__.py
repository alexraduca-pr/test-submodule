{
    "name": "Modulo dati corso funzionale",
    "summary": "Modulo dati eLearning del corso funzionale",
    "description": """
    Modulo che importa i dati e configura il modulo eLearning del corso funzionale, installandolo se mancante
    """,
    "author": "PR Consulting",
    "version": "19.0.1.0.0",
    "category": "PR Consulting/Training",
    "depends": ["base", "website_slides"],
    "data": [
        "data/attachments.xml",
        "data/website_slides.xml",
        "data/website_slides_section_2.xml",
        "data/website_slides_section_3.xml",
        "data/website_slides_section_4.xml",
        "data/post_links.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
