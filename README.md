<img src="https://img.freepik.com/free-photo/magnified-single-yellow-fish-eye-with-abstract-pattern-generated-by-ai_188544-9714.jpg"></img>

# Cas Pratique : Reconnaissance d'iris

Ceci est le dépôt du **cas pratique** présenté pour le passage de titre de l'école Microsoft IA par Simplon et Isen, promotion 2023-2024 de Caen. 

## TODO

- Quelques problèmes sur le notebook 'ID gauche'
- Notebook : 'ID right' classifier
- Streamlit app
- Rapport
- Article blog dev/medium
- Update readme.md

## Description du cas pratique

Vous êtes un développeur IA, votre entreprise vous a confié la mission de **développer une interface de reconnaissance d’oeil pour une entreprise souhaitant authentifier ses 45 employés** à partir d’un scan de leurs yeux.

## Description des dossiers de ce dépôt

- **Consignes** : ensemble des consignes et des données pour mener le projet.
- **Notebooks** : les notebooks ou sont créés et entrainé les modèles de Deep Learning. 
- Models : les différents modèles entrainés sur les données.
- App : application front-end pour effectuer les prédictions à partir de photos d'yeux.

## Notebooks

Notebooks de création des modèles de Deep Learning. L'architecture utilisée est :
- un modèle VGG16 entrainé sur ImageNet. 
- une couche de sortie entrainable qui correspond au nombre de nos classes cibles.

Cette architecture est un cas de **Transfer Learning**. Pour créer ces modèle de reconnaissance d'image, nous utilisons un modèle pré-entrainé auquel nous ajoutons une ou des couches entrainables sur nos données d'entrainement (les photos d'yeux des employés).

### Partie 1 : Classification oeil gauche ou droit

Développement d'un classificateur qui détecte si l'image est un oeil gauche ou un oeil droit.

### Partie 2 : Classification ID employé (oeil gauche)

Développement d'un **classificateur** qui retrouve l'identifiant d'un employé à partir de l'image de son oeil gauche.

### Partie 3 : Classification ID employé (oeil droit)

Développement d'un **classificateur** qui retrouve l'identifiant d'un employé à partir de l'image de son oeil droit.

## Application Streamlit

Développement d'une application Streamlit pour offir une interface aux utilisateurs et réaliser des inférences à partir de photos d'oeils. 

- https://streamlit.io/

## A propos 

Projet développé par **David Scanu**. Étudiant en intelligence artificielle 🤖 à l'**École Microsoft IA par Simplon et ISEN**, 1ère promotion de Caen.

- Twitter
- Dev
- Medium 
- Instagram
- LinkedIn

## Description de l'école Microsoft 
