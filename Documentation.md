# OriSup

**OriSup** est une solution basée sur l'Intelligence Artificielle visant à orienter les étudiants dans le choix de leur formation au sein du réseau universitaire marocain.

---

## Structure du projet

La structure du projet est organisée comme suit :

```
ORISUP/
├── .github/workflows/
│   └── docker-build-push.yml  # Workflow CI/CD pour la construction et le déploiement Docker
├── img/
│   ├── logo_orisup.ico        # Icône du logo OriSup
│   ├── logo_orisup.jpg        # Image du logo OriSup
├── landingpage/
│   ├── css/                   # Feuilles de style CSS pour la page d'accueil
│   ├── img/                   # Images supplémentaires pour la page d'accueil
│   ├── js/                    # Scripts JavaScript pour la page
│   ├── lib/                   # Librairies externes utilisées
│   ├── scss/                  # Fichiers SCSS (styles avancés)
│   └── index.html             # Page HTML principale
├── .env                       # Fichier d'environnement (variables sensibles)
├── .gitignore                 # Fichiers et dossiers ignorés par Git
├── cal_mean.py                # Script Python pour le calcul des moyennes (exemple : analyse des données)
├── chatbot.py                 # Script Python pour le chatbot d'orientation
├── data_university.txt        # Données des universités marocaines
├── Dockerfile                 # Configuration Docker pour l'application
├── ISTA_maroc.txt             # Données spécifiques aux ISTA au Maroc
└── LICENSE.txt                # Licence du projet
```

---

## Prérequis

Avant de commencer, assurez-vous que votre système dispose des éléments suivants :

- **Python 3.8 ou supérieur** installé
- **Docker** pour le déploiement
- **Git** pour cloner le projet
- Librairies Python nécessaires (listées dans `requirements.txt` ou `chatbot.py`)

---

## Installation et utilisation

### 1. Cloner le projet
```bash
git clone https://github.com/votre-repo/orisup.git
cd orisup
```

### 2. Configurer l'environnement
Créez un fichier `.env` basé sur les variables nécessaires (voir `.env.example` si disponible).

### 3. Installer les dépendances
Assurez-vous d’installer les dépendances Python avec :
```bash
pip install -r requirements.txt
```

### 4. Lancer l'application localement
- **Pour le chatbot** :
```bash
python chatbot.py
```

- **Pour la landing page** :
Ouvrez `landingpage/index.html` dans un navigateur.

### 5. Utilisation avec Docker
Construire et exécuter l'application avec Docker :
```bash
docker build -t orisup .
docker run -p 8000:8000 orisup
```

### 5. Utilisation avec Nom de domaine

```bash
python -m http.server 80
```

---

## Développement

### Contribution
Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le dépôt.
2. Créez une branche de fonctionnalité :
   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalite
   ```
3. Soumettez une pull request.

### Tests
Des tests unitaires doivent être ajoutés pour toutes les nouvelles fonctionnalités. Lancez-les avec :
```bash
pytest
```

---

## CI/CD

Un workflow GitHub Actions est configuré pour :
- Construire automatiquement l'image Docker (`docker-build-push.yml`).
- Déployer sur un registre ou une plateforme compatible (exemple : Docker Hub).

---

## Licence

Ce projet est sous licence **[MIT](LICENSE.txt)**. Veuillez consulter le fichier `LICENSE.txt` pour plus de détails.


## Contact

Pour toute question ou suggestion, veuillez contacter l'équipe de développement ou ouvrir une **issue** sur le dépôt GitHub.
