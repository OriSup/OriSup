import requests
import json
import os
from dotenv import load_dotenv
import streamlit as st




load_dotenv()

api_key = os.environ.get("api_key")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

headers = {
  'Content-Type': 'application/json'
}

with open("./data_university.txt", "r") as file:
    data = file.read()


st.title("Assistant d'Orientation Universitaire")

nom = st.text_input("Nom de l'étudiant:")
prenom = st.text_input("Prénom de l'étudiant:")
age = st.number_input("Âge de l'étudiant:", min_value=18, max_value=100, step=1)
domaine_etude = st.text_input("Domaine d'étude préféré:")
niveau_etude = st.selectbox("Niveau d'étude:", ["Bac", "Licence", "Master", "Doctorat"])


template = lambda prompt:  [
        {
          "text": f"""message system: Tu es un assistant et conseiller d'orientation des etudiants sur le choix de leur formation dans le reseau universitaire marocain. 
          Tu extrais les informations personnelles et academiques de l'etudiant et lui proposer une bonne formation dans une université marocaine. Précis, concis, sarcastique et jovial pour les etudiant.
          Cherche les informations sur les autres sources.
          """
        },
        {
          "text": f"""
            prompt: Je suis {nom} {prenom}, j'ai {age} ans. Niveau d'etude: {niveau_etude}. Domaine preféré: {domaine_etude}. Ma question est: {prompt} .
            données sur les universités: {data}
            """
        }
      ]


prompt = st.text_area("Votre question ou demande d'orientation:")

if st.button("Obtenir une recommandation"):
    if prompt and nom and prenom:

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
        
        if response.status_code == 200:
            st.write(f"Chat: {response.json()['candidates'][0]['content']['parts'][0]['text']}")
        else:
            st.error("Erreur lors de la récupération des données.")
    else:
        st.warning("Veuillez remplir tous les champs nécessaires.")
