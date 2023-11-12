import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
# import cv2

import os
import random
import datetime
import shutil
import io
import pickle
import json

import tensorflow as tf
from sklearn.preprocessing import LabelEncoder

# Fucntions
def check_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


# Variables 
img_width = 320
img_height = 240
img_channels = 3
img_dim = (img_height, img_width, img_channels)


# Employees JSON
with open("employees_info.json", 'r') as f:
    employees_dict = json.load(f)

# LEFT-RIGHT
# LR Classifier Model
lr_classifier_path = "./models/lr_classifier.h5"
lr_classifier_restored = tf.keras.models.load_model(lr_classifier_path)
# LR Label Encoder
lr_label_encoder_path = "./models/lr_label_encoder.pkl"
with open(lr_label_encoder_path, 'rb') as f:
    lr_label_encoder = pickle.load(f) # deserialize using load()
# Prédiction Gauche-Droite
def inference_lr(image_file, label_encoder):
    """
    Fonction de prédiction du côté (gauche ou droite) de l'oeil
    à partir d'un fichier image (ndarray ou PIL Image).
    """
    # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
    image_file_more_dims = np.expand_dims(image_file, axis=0)
    # Inférence
    pred = np.argmax(lr_classifier_restored.predict(image_file_more_dims), axis=1)[0]
    # Désencodage de l'index de classe en classe (string)
    pred_class_str = label_encoder.classes_[pred]
    # Retourne une string
    return pred_class_str

# ID Employé (gauche)
# ID Left Classifier Model
id_left_classifier_path = "./models/id_left_classifier.h5"
id_left_classifier_restored = tf.keras.models.load_model(id_left_classifier_path)
# Prédiction ID employé (oeil gauche)
# Prédiction Gauche-Droite
def inference_id_left(image_file) -> int:
    """
    Fonction de prédiction de l'ID de l'employé à partir 
    d'un fichierimage de son oeil gauche(ndarray ou PIL Image).

    Retourne l'ID de l'employé (str).
    """
    # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
    image_file_more_dims = np.expand_dims(image_file, axis=0)
    # Inférence, 
    id_employee = int(np.argmax(id_left_classifier_restored.predict(image_file_more_dims), axis=1)[0])
    print(id_left_classifier_restored.predict(image_file_more_dims))
    # Retourne l'identifiant de l'employé (int)
    return id_employee

def find_employee_infos(id_employee):
    """
    Retourne les informations de l'employé grace à son identifiant (ID)
    """
    return employees_dict[str(id_employee)]


# ID Employé (droite)
# prédiction ID employé (oeil droit)



# Streamlit App
st.set_page_config(
    page_title="Reconnaissance d'iris",
    page_icon="👀",
    layout="centered"
)


# Header
st.header("Reconnaissance d'iris 👀", divider='rainbow')
st.markdown("Une applicaton pour la **reconnaissance d’iris** pour authentifier vos employés.")
st.markdown("""Développé par **David Scanu** &mdash; Normand'IA 2023-2024""")
st.divider()

# List
image = st.file_uploader(
    "Choisissez une image",
    type=['png', 'jpg', 'jpeg', 'bmp'],
    accept_multiple_files=False,
    label_visibility="visible"
)
if image is not None:
    bytes_data = image.read() # bytes
    image_pil = Image.open(io.BytesIO(bytes_data)) # PIL Object
    # Montrer l'image dans le navigateur
    st.image(image_pil)
    with st.spinner('Wait for it...'):
        # Détection du côté de l'oeil
        lr_pred = inference_lr(image_pil, lr_label_encoder)
        # Oeil gauche
        if lr_pred == 'left':
            st.success('Oeil détecté : Gauche')
            id_employee = inference_id_left(image_pil)
            dict_employee = find_employee_infos(id_employee)
            st.markdown(f"""
                        # {dict_employee['nom']}
                        - ID employé(e) : {id_employee}
                        - Poste : {dict_employee['poste']} 
                        - Année d'embauche : {dict_employee['annee_embauche']}
                        - Genre : {dict_employee['genre']}
                        """)
        # Oeil droite
        elif lr_pred == 'right':
            st.success('Right!')