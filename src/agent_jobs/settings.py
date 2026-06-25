from __future__ import annotations

HOME_CITY = "Sens"
HOME_POSTAL_CODE = "89100"
HOME_COUNTRY = "France"
HOME_LAT = 48.1974
HOME_LON = 3.2833
RADIUS_KM = 80
MAX_RESULTS_EMAIL = 35

CONTRACT_TERMS = [
    "alternance", "apprentissage", "stage", "internship", "intership", "graduate program",
    "graduate programme", "graduate", "trainee program", "VIE"
]

ROLE_TERMS = [
    "data engineer", "big data engineer", "expert big data", "ingénieur data", "ingenieur data",
    "chef de projet data", "project manager data", "mlops", "data scientist",
    "ingénieur IA", "ingenieur IA", "ai engineer", "machine learning engineer",
    "ingénieur logiciel", "ingenieur logiciel", "software engineer", "systèmes embarqués",
    "systeme embarque", "embedded software", "robotique", "automatique", "intégration système",
    "integration systeme", "electronic", "électronique", "hardware", "firmware"
]

SECTOR_TERMS = [
    "IA", "intelligence artificielle", "data", "big data", "nouvelles technologies",
    "industrie 4.0", "cloud", "MLOps", "LLMOps", "RAG", "cybersécurité",
    "énergie", "energie", "oil and gas", "pétrole", "gaz", "minier", "mine",
    "mining", "nucléaire", "nucleaire", "électricité", "electricite", "robotique", "hVAC", "HVAC"
]

PRIORITY_COMPANIES = [
    "TotalEnergies", "Safran", "Framatome", "EDF", "Orano", "CEA", "Schneider Electric",
    "Air Liquide", "Technip Energies", "Vallourec", "Eramet", "Imerys", "Thales",
    "Alstom", "SUEZ", "Veolia", "Assystem", "Akkodis", "Capgemini", "Atos", "Eviden",
    "Randstad", "Sopra Steria", "ArianeGroup", "Bouygues Energies", "SPIE"
]

TARGET_SITES = [
    "linkedin.com/jobs", "glassdoor.fr", "indeed.com", "indeed.fr", "apec.fr", "hellowork.com",
    "teamtailor.com", "jobup.ch", "francetravail.fr", "randstad.fr", "careers.totalenergies.com",
    "safran-group.com", "framatome.com", "edf.fr", "orano.group", "cea.fr", "welcometothejungle.com"
]

# Villes prioritaires dans un rayon proche de Sens ou pertinentes pour l'énergie/data.
NEARBY_LOCATIONS = {
    "sens": (48.1974, 3.2833), "89100": (48.1974, 3.2833),
    "yonne": (47.8653, 3.6079), "auxerre": (47.7982, 3.5738), "montereau": (48.3833, 2.9500),
    "montereau-fault-yonne": (48.3833, 2.9500), "fontainebleau": (48.4047, 2.7016),
    "nemours": (48.2670, 2.6960), "provins": (48.5589, 3.2998), "troyes": (48.2973, 4.0744),
    "aube": (48.3202, 4.1905), "nogent-sur-seine": (48.4936, 3.5026), "montargis": (47.9976, 2.7326),
    "orleans": (47.9029, 1.9093), "orléans": (47.9029, 1.9093), "paris": (48.8566, 2.3522),
    "ile-de-france": (48.8566, 2.3522), "île-de-france": (48.8566, 2.3522),
    "belfort": (47.6386, 6.8628), "dijon": (47.3220, 5.0415), "besançon": (47.2380, 6.0240),
    "besancon": (47.2380, 6.0240), "genève": (46.2044, 6.1432), "geneve": (46.2044, 6.1432),
    "lausanne": (46.5197, 6.6323), "neuchâtel": (46.9896, 6.9293), "neuchatel": (46.9896, 6.9293),
    "fribourg": (46.8065, 7.1619), "suisse romande": (46.5197, 6.6323)
}
