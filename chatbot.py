import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("api_key")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

headers = {
  'Content-Type': 'application/json'
}


template = lambda prompt:  [
        {
          "text": f"""Tu es un assistant et conseiller d'orientation des etudiants sur le choix de leur formation dans le reseau universitaire marocain. 
          Tu extrais les informations personnelles et academiques de l'etudiant et lui proposer une bonne formation dans une université marocaine."""
        },
        {
          "text": prompt
        }
      ]

while True:
    print("Chat: Bonjour qu'est-ce que je peux faire pour vous ? Rien pour quitter")
    print("_"*50)
    prompt = input("Etudiant: ")
    print("_"*50)
    if(prompt == "Rien"):
        print("Chat: Bye!!!")
        break
    
    payload = json.dumps({
    "contents": [
        {
        "parts": template(prompt)
        }
    ],
    "generation_config": {
        "temperature": 0.1
    }
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    if(response.status_code == 200 ):
        print(f'''Chat: {response.json()["candidates"][0]["content"]["parts"][0]["text"]}''')

    
    print("_"*50)




