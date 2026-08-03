COMPANIES = [

    "OpenAI",

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
            "AI Data Engineer",

            "company":
            company,

            "location":
            "Europe",

            "description":
            "AI Big Data Machine Learning",

            "contract":
            "Graduate Junior",

            "link":
            "https://careers.google.com"

        })


    return jobs