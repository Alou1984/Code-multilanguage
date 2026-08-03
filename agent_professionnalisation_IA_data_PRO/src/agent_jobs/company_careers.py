import requests
from bs4 import BeautifulSoup


COMPANIES = {

    # IA / Tech

    "OpenAI":
    "https://openai.com/careers",

    "Anthropic":
    "https://www.anthropic.com/careers",

    "NVIDIA":
    "https://www.nvidia.com/en-us/about-nvidia/careers/",

    "Google":
    "https://careers.google.com",

    "Microsoft":
    "https://careers.microsoft.com",

    "Amazon":
    "https://www.amazon.jobs",


    # IA Europe

    "Mistral AI":
    "https://mistral.ai/careers",

    "Hugging Face":
    "https://huggingface.co/jobs",

    "Dataiku":
    "https://www.dataiku.com/careers",


    # Industrie

    "Airbus":
    "https://www.airbus.com/en/careers",

    "Safran":
    "https://www.safran-group.com/jobs",

    "Thales":
    "https://careers.thalesgroup.com",

    "EDF":
    "https://www.edf.fr/edf-recrute",

    "TotalEnergies":
    "https://careers.totalenergies.com",

    "Framatome":
    "https://www.framatome.com/careers",

    "STMicroelectronics":
    "https://careers.st.com",


    # Industrie mondiale

    "Siemens":
    "https://jobs.siemens.com",

    "Schneider Electric":
    "https://www.se.com/careers",

    "Bosch":
    "https://www.bosch.com/careers",

    "ABB":
    "https://careers.abb.com",


    # Energie / Mining

    "BP":
    "https://careers.bp.com",

    "Shell":
    "https://www.shell.com/careers",

    "BHP":
    "https://careers.bhp.com",

    "Rio Tinto":
    "https://www.riotinto.com/careers"

}



KEYWORDS = [

    "data",

    "ai",

    "artificial intelligence",

    "machine learning",

    "ml",

    "deep learning",

    "llm",

    "python",

    "cloud",

    "robotics",

    "big data",

    "mlops"

]



def search_company_jobs():


    jobs=[]


    for company,url in COMPANIES.items():


        try:


            response=requests.get(

                url,

                timeout=15,

                headers={

                    "User-Agent":
                    "Mozilla/5.0"

                }

            )


            if response.status_code != 200:

                continue



            soup=BeautifulSoup(

                response.text,

                "html.parser"

            )



            for link in soup.find_all(
                "a",
                href=True
            ):


                title=link.text.strip()


                href=link["href"]



                text=(

                    title

                    +

                    " "

                    +

                    href

                ).lower()



                if not any(

                    word in text

                    for word in KEYWORDS

                ):

                    continue



                if href.startswith("/"):

                    href=url.rstrip("/") + href



                jobs.append({

                    "title":

                    title,


                    "company":

                    company,


                    "location":

                    "International",


                    "description":

                    "Career page IA/Data",


                    "contract":

                    "",


                    "link":

                    href

                })



        except Exception as e:


            print(

                "CAREER ERROR",

                company,

                e

            )



    return jobs