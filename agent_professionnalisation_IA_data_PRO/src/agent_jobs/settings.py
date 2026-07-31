import os


HOME_CITY = "Sens"
HOME_POSTAL_CODE = "89100"
RADIUS_KM = 80


EMAIL_TO = os.getenv("EMAIL_TO")


TARGET_CONTRACTS = [
    "contrat professionnalisation",
    "graduate program",
    "apprentissage",
    "alternance"
]


TARGET_ROLES = [

    "Expert Big Data Engineer",
    "Big Data Engineer",
    "Data Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "MLOps Engineer",
    "LLM Engineer",
    "Deep Learning Engineer",
    "Data Scientist",
    "Chef de projet Data",
    "Cloud Engineer"
]


TARGET_DOMAINS = [

    "intelligence artificielle",
    "IA",
    "machine learning",
    "deep learning",
    "LLM",
    "GPU",
    "data",
    "big data",

    "énergie",
    "oil",
    "gas",
    "mining",
    "nucléaire",

    "aéronautique",
    "aérospatial",
    "robotique",
    "système embarqué",
    "électronique"
]


TARGET_COMPANIES = [

    "EDF",
    "TotalEnergies",
    "Safran",
    "Framatome",
    "Airbus",
    "Eramet",
    "BHP",
    "BP",
    "Prysmian",
    "Alstom",
    "NVIDIA"
]


LOCATIONS = [

    # France
    "France",
    "Ile-de-France",
    "Paris",
    "Bourgogne-Franche-Comté",
    "Centre-Val de Loire",
    "Sens France",
    "Lyon France",
    "Toulouse France",
    "Grenoble France",

    # Europe
    "Suisse",
    "Suisse Romande",
    "Genève Suisse",
    "Lausanne Suisse",
    "Luxembourg",
    "Royaume-Uni",
    "London UK",
    "Manchester UK",

    # Moyen-Orient
    "United Arab Emirates",
    "Dubai UAE",
    "Abu Dhabi UAE",
    "Saudi Arabia",
    "Riyadh Saudi Arabia",
    "Jeddah Saudi Arabia",

    # Amérique du Nord
    "United States",
    "USA",
    "New York USA",
    "California USA",
    "San Francisco USA",
    "Seattle USA",
    "Texas USA",

    # Remote
    "Remote",
    "Full Remote",
    "Remote Worldwide",
    "Worldwide Remote"

]