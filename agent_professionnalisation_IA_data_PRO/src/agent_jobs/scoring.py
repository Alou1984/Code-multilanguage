SKILLS_SCORE = {


    "llm": 25,

    "large language model": 25,

    "generative ai": 20,

    "gpu": 20,

    "cuda": 20,

    "nvidia": 20,


    "machine learning": 15,

    "deep learning": 15,


    "python": 10,

    "spark": 10,

    "hadoop": 10,


    "mlops": 15,

    "kubernetes": 10,


    "aws": 10,

    "cloud": 10,


    "robotique": 15,

    "embedded": 15,

    "système embarqué": 15,


    "aéronautique": 15,

    "aérospatial": 15,


    "oil": 10,

    "gas": 10,

    "mining": 10,

    "energy": 10

}



def score_offer(job):


    text = (

        job["title"]

        + " "

        + job["description"]

        + " "

        + job["company"]

    ).lower()



    score = 0



    for keyword, points in SKILLS_SCORE.items():


        if keyword in text:


            score += points



    job["score"] = score



    return job



def score_jobs(jobs):


    return [

        score_offer(job)

        for job in jobs

    ]