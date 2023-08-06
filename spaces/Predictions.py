import requests
from decouple import config




def predictEmtions(text):
    url = "https://sentiment-analysis9.p.rapidapi.com/sentiment"

    payload = [
        {
            "id": "1",
            "language": "en",
            "text":f"{text}"
        }
    ]
    headers = {
        "content-type": "application/json",
        "Accept": "application/json",
        "X-RapidAPI-Key": config("emtions_api"),
        "X-RapidAPI-Host": "sentiment-analysis9.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()



