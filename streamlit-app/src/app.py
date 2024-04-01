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
lr_classifier_path = "./models/lr_classifier_v3.h5"
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
    pred = lr_classifier_restored.predict(image_file_more_dims)
    pred_max = np.argmax(pred, axis=1)[0]
    # Désencodage de l'index de classe en classe (string)
    pred_class = label_encoder.classes_[pred_max]
    pred_score = np.max(pred)
    # Retourne une string
    return pred_class, pred_score


# ID Employé
# ID Left Classifier Model
id_left_classifier_path = "./models/id_left_classifier_v3.h5"
id_left_classifier_restored = tf.keras.models.load_model(id_left_classifier_path)
# ID Right Classifier Model
id_right_classifier_path = "./models/id_right_classifier_v3.h5"
id_right_classifier_restored = tf.keras.models.load_model(id_right_classifier_path)
# ID Label Encoder
id_label_encoder_path = "./models/id_label_encoder.pkl"
with open(id_label_encoder_path, 'rb') as f:
    id_label_encoder = pickle.load(f) # deserialize using load()

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



# Streamlit App
st.set_page_config(
    page_title="Eye Detector",
    page_icon=":eye-in-speech-bubble:",
    layout="centered"
)

# Header
st.image('images/cover-02.jpg')
st.header(":eye-in-speech-bubble: Eye Detector", divider='rainbow')
st.markdown("Une applicaton de **reconnaissance d’iris** pour authentifier vos employés.")


# Image Uploader
st.markdown("### Choisissez une image")
image = st.file_uploader(
    label="Choisissez une image",
    type=['png', 'jpg', 'jpeg', 'bmp'],
    accept_multiple_files=False,
    label_visibility="collapsed"
)
if image is not None:
    bytes_data = image.read() # bytes
    image_pil = Image.open(io.BytesIO(bytes_data)) # PIL Object
    with st.spinner('Wait for it...'):
        # Détection du côté de l'oeil
        lr_pred_class, lr_pred_score = inference_lr(image_pil, lr_label_encoder)
        # Oeil gauche
        if lr_pred_class == 'left':
            st.success(f"Oeil détecté : Gauche &mdash; (Score de prédiction : {lr_pred_score:.2%})")
        # Oeil droite
        elif lr_pred_class == 'right':
            st.success(f"Oeil détecté : Droit &mdash; (Score de prédiction : {lr_pred_score:.2%})")

col1, col2 = st.columns(2)

with col1:
    if image is not None:
        # Montrer l'image dans le navigateur
        st.image(image_pil)

with col2:
    # Détection ID + informations de l'employé
    if image is not None:
        with st.spinner('Wait for it...'):
          # Prédiction ID de l'employé
          employee_id, employee_score = id_inference(image_pil, lr_pred_class)
          dict_employee = find_employee_infos(employee_id)
          st.markdown(f"""
                      # {dict_employee['nom']}
                      - ID employé(e) : {employee_id}
                      - Poste : {dict_employee['poste']} 
                      - Année d'embauche : {dict_employee['annee_embauche']}
                      - Genre : {dict_employee['genre']}
                      """)
          st.caption(f"Score de prédiction : {employee_score:.2%}")

st.divider()

"""
> 🎓 Projet développé par [David Scanu](https://www.linkedin.com/in/davidscanu14/), étudiant en intelligence artificielle 🤖 à l'[École Microsoft IA Caen par Simplon et ISEN](https://isen-caen.fr/ecole-ia-microsoft-by-simplon-et-isen-ouest/), 1ère promotion de Caen (2023-2024).
"""