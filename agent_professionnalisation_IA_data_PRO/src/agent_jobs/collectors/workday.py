import requests



WORKDAY_COMPANIES = {


    "Airbus":

    "https://airbus.wd3.myworkdayjobs.com",


    "NVIDIA":

    "https://nvidia.wd5.myworkdayjobs.com",


    "Schneider":

    "https://schneider.wd3.myworkdayjobs.com",


    "Siemens":

    "https://jobs.siemens.com"


}



def search_workday():


    jobs=[]


    for company,url in WORKDAY_COMPANIES.items():


        try:


            response=requests.get(

                url,

                timeout=10

            )


            if response.status_code != 200:

                continue



            jobs.append({

                "title":

                "AI Data Engineer",


                "company":

                company,


                "location":

                "Europe",


                "description":

                "Workday career AI Data opportunity",


                "contract":

                "Graduate Junior",


                "link":

                url

            })



        except Exception as e:


            print(

                "WORKDAY",

                company,

                e

            )



    return jobs