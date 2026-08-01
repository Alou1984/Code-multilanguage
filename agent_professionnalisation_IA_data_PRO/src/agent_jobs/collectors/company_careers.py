import requests



COMPANIES = {

"EDF":
"https://www.edf.fr",

"SAFRAN":
"https://www.safran-group.com",

"Airbus":
"https://www.airbus.com",

"TotalEnergies":
"https://totalenergies.com",

"Thales":
"https://www.thalesgroup.com"

}



KEYWORDS=[

"data engineer",

"ai engineer",

"machine learning",

"big data",

"mlops"

]



def search_company_careers():


    jobs=[]


    for company,url in COMPANIES.items():


        for keyword in KEYWORDS:


            jobs.append({

                "title":
                keyword,

                "company":
                company,

                "location":
                "Europe",

                "description":
                f"Recherche carrière {keyword}",

                "link":
                url

            })


    return jobs