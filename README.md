<img src="https://img.freepik.com/free-photo/magnified-single-yellow-fish-eye-with-abstract-pattern-generated-by-ai_188544-9714.jpg"></img>

# 👁️‍🗨️ E2 - Cas Pratique 1 : "Reconnaissance d'iris"

Ce **cas pratique : "Reconnaissance d'iris"** témoigne de la maîtrise des compétences visées pour l'obtention du titre professionnel : [Développeur en intelligence artificielle (RNCP 34757)](https://www.francecompetences.fr/recherche/rncp/34757/), délivré par [Simplon](https://simplon.co/), dans le cadre de l'[École Microsoft IA Caen par Simplon et ISEN](https://isen-caen.fr/ecole-ia-microsoft-by-simplon-et-isen-ouest/). Ce cas pratique implique l'amélioration d'un modèle de vision par ordinateur, ainsi que le développement d'une application web qui le déploie.

> 🎓 Projet développé par [David Scanu](https://www.linkedin.com/in/davidscanu14/), étudiant en intelligence artificielle 🤖 à l'[École Microsoft IA Caen par Simplon et ISEN](https://isen-caen.fr/ecole-ia-microsoft-by-simplon-et-isen-ouest/), 1ère promotion de Caen (2023-2024).

| | | |
| --- | --- | --- |
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/davidscanu14/) | [![image alt text](https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=dev.to&logoColor=white)](https://dev.to/davidscanu) | [![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://davidscanu.medium.com/) |

## Description du cas pratique

Vous êtes un développeur IA, votre entreprise vous a confié la mission de **développer une interface de reconnaissance d’oeil pour une entreprise souhaitant authentifier ses 45 employés** à partir d’un scan de leurs yeux.

## Description des dossiers

- `consignes` : Ensemble des consignes et des données pour mener le projet.
- `Notebooks` : Les notebooks ou sont créés et entrainé les modèles de reconnaissance d'iris. 
- `streamlit-app` : Application front-end pour effectuer les prédictions à partir de photos d'yeux.

## Notebooks

Notebooks de création des modèles de Deep Learning. L'architecture utilisée est :
- un modèle VGG16 entrainé sur ImageNet. 
- une couche de sortie entrainable qui correspond au nombre de nos classes cibles.

Cette architecture est un cas d'**apprentissage par transfert** (Transfer Learning). Pour créer ces modèle de reconnaissance d'image, nous utilisons un modèle pré-entrainé auquel nous ajoutons une ou des couches entrainables sur nos données d'entrainement (les photos d'yeux des employés).

| Notebook | Colab | Description |
| --- | --- | --- |
| Classification oeil gauche ou droit | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1cg7OEodKzWm7EfX8qJu7TtNNoKGIWnP2?usp=sharing) | Développement d'un classificateur qui détecte si l'image est un oeil gauche ou un oeil droit. |
| Classification ID employé | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1F8Cbeu2GZvBhng_A4p9V-SdSLqAF2JEU?usp=sharing) | Développement d'un **classificateur** qui retrouve l'identifiant d'un employé à partir de l'image de son oeil gauche ou de son oeil droit ( 2 modèles) |

## Application Streamlit

Développement d'une application Streamlit pour offir une interface aux utilisateurs et réaliser des prédictions à partir de photos d'yeux. 

<img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" alt="Streamlit Logo" width=320>