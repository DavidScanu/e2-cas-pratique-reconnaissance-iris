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
import keras
from sklearn.preprocessing import LabelEncoder

# Fucntions
def check_file_exists(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

# keras.config.enable_unsafe_deserialization()

# Variables 
img_width = 320
img_height = 240
img_channels = 3
img_dim = (img_height, img_width, img_channels)

# Models path
lr_classifier_path = "./models/v4/lr-v4-vgg16.h5"
id_left_classifier_path = "./models/v4/id-left-xception.keras"
id_right_classifier_path = "./models/v4/id-right-xception.keras"
# label encoders path
lr_label_encoder_path = "./models/v4/lr-label-encoder.pkl"
id_label_encoder_path = "./models/v4/id_label_encoder.pkl"

# Employees JSON
with open("employees_info.json", 'r') as f:
    employees_dict = json.load(f)


# Streamlit App
st.set_page_config(
    page_title="Eye Detector",
    page_icon=":eye-in-speech-bubble:",
    layout="centered"
)

# LEFT-RIGHT
# LR Classifier Model
@st.cache_resource
def load_lr_model(model_path):
    lr_model = keras.models.load_model(model_path)
    return lr_model
lr_classifier_restored = load_lr_model(lr_classifier_path)

# LR Label Encoder
with open(lr_label_encoder_path, 'rb') as f:
    lr_label_encoder = pickle.load(f)

# Prédiction Gauche-Droite
def inference_lr(image_file, label_encoder):
    """
    Fonction de prédiction du côté (gauche ou droite) de l'oeil
    à partir d'un fichier image (ndarray ou PIL Image).
    """
    # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
    image_file_more_dims = np.expand_dims(image_file, axis=0)
    # Inférence
    pred = lr_classifier_restored.predict(image_file_more_dims)
    pred_max = np.argmax(pred, axis=1)[0]
    # Désencodage de l'index de classe en classe (string)
    pred_class = label_encoder.classes_[pred_max]
    pred_score = np.max(pred)
    # Retourne une string
    return pred_class, pred_score


# ID Employé

# ID Left Classifier Model
@st.cache_resource
def load_id_left_model(model_path):
    id_left_model = keras.models.load_model(model_path)
    return id_left_model
id_left_classifier_restored = load_id_left_model(id_left_classifier_path)

# ID Right Classifier Model
@st.cache_resource
def load_id_right_model(model_path):
    id_right_model = keras.models.load_model(model_path)
    return id_right_model
id_right_classifier_restored = load_id_right_model(id_right_classifier_path)

# ID Label Encoder
with open(id_label_encoder_path, 'rb') as f:
    id_label_encoder = pickle.load(f)

# Prédiction ID employé
def id_inference(image_file, side):
  """
  Fonction qui réalise une prédiction à partir d'un fichier image (ndarray ou PIL Image).
  """
  # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
  image_file_more_dims = np.expand_dims(image_file, axis=0)
  # Détection de l'index de l'ID de l'employé
  if side == 'left':
    pred = id_left_classifier_restored.predict(image_file_more_dims)
  elif side == 'right':
    pred = id_right_classifier_restored.predict(image_file_more_dims)  
  pred_index = np.argmax(pred, axis=1)[0]
  # Désencodage de l'index de classe en classe (string)
  pred_class = int(id_label_encoder.classes_[pred_index])
  # Score de la prédiction
  pred_score = np.max(pred)
  # Retourne l'ID de l'employé détecté (int)
  return pred_class, pred_score


# Obtenir les informations de l'employé à partir de son identifiant (ID)
def find_employee_infos(id_employee):
    """
    Retourne les informations de l'employé grace à son identifiant (ID)
    """
    return employees_dict[str(id_employee)]





# Header
st.sidebar.image('images/cover-02.jpg')
st.sidebar.header(":eye-in-speech-bubble: Eye Detector", divider='rainbow')
st.sidebar.markdown("Une applicaton de **reconnaissance d’iris** pour authentifier vos employés.")

# Image Uploader
st.sidebar.markdown("### Choisissez une image")
image = st.sidebar.file_uploader(
    label="Choisissez une image",
    type=['png', 'jpg', 'jpeg', 'bmp'],
    accept_multiple_files=False,
    label_visibility="collapsed"
)

if image is not None:
    with st.spinner('Wait for it...'):
        # Détection du côté de l'oeil
        bytes_data = image.read() # bytes
        image_pil = Image.open(io.BytesIO(bytes_data)) # PIL Object
        lr_pred_class, lr_pred_score = inference_lr(image_pil, lr_label_encoder)
        if lr_pred_score:
            with st.container(border=True):
                # Oeil gauche
                if lr_pred_class == 'left':
                    st.subheader("👁️ Oeil détecté : Oeil gauche 👈")
                # Oeil droite
                elif lr_pred_class == 'right':
                    st.subheader("👁️ Oeil détecté : Oeil droit 👉")
                st.success(f"Score de prédiction : **{lr_pred_score:.2%}**")
        else:
            st.error("Une erreure s'est produite.")


if image is not None:
    # Prédiction ID de l'employé          
    employee_id, employee_score = id_inference(image_pil, lr_pred_class)
    dict_employee = find_employee_infos(employee_id)
    with st.spinner('Wait for it...'):
        with st.container(border=True):
            st.header(f"Bienvenue {dict_employee['nom']} !")
            col1, col2 = st.columns(2)
            with col1:
                st.image(image_pil)
            with col2:
                st.markdown(f"""
                            - 🔐 ID employé(e) : :blue[{employee_id}]
                            - 💼 Poste : {dict_employee['poste']} 
                            - 📅 Année d'embauche : {dict_employee['annee_embauche']}
                            - 👫 Genre : {dict_employee['genre']}
                            """)
            if employee_score is not None:
                st.success(f"Score de prédiction : **{employee_score:.2%}**")
            

# st.sidebar.divider()
# st.sidebar.markdown(
#     """
#     🎓 Projet développé par [David Scanu](https://www.linkedin.com/in/davidscanu14/), étudiant en intelligence artificielle 🤖 à l'[École Microsoft IA Caen par Simplon et ISEN](https://isen-caen.fr/ecole-ia-microsoft-by-simplon-et-isen-ouest/), 1ère promotion de Caen (2023-2024).
#     """
# )
