COMPANIES = [

    "OpenAI",

    "Anthropic",

    "NVIDIA",

    "Google",

    "Microsoft",

    "Amazon",

    "Mistral AI",

    "Hugging Face",

    "Dataiku",

    "Airbus",

    "Safran",

    "Thales",

    "EDF",

    "TotalEnergies",

    "Framatome",

    "STMicroelectronics",

    "Schneider Electric",

    "Siemens",

    "BHP",

    "Rio Tinto"

]



def search_company_jobs():


    jobs=[]


    for company in COMPANIES:


        jobs.append({

            "title":
            "AI Engineer / Data Engineer",


            "company":
            company,


            "location":
            "Europe",


            "description":
            """
            Artificial Intelligence,
            Big Data,
            Machine Learning,
            Deep Learning,
            Data Engineering
            """,


            "contract":
            "Graduate Junior",


            "link":
            "https://www.google.com/search?q="
            + company
            + "+careers"

        })


    return jobs