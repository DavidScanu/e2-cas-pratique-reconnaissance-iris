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

# LR Model
lr_classifier_path = "./models/lr_classifier.h5"
lr_classifier_restored = tf.keras.models.load_model(lr_classifier_path)
# LR Label Encoder
lr_label_encoder_path = "./models/lr_label_encoder.pkl"
with open(lr_label_encoder_path, 'rb') as f:
  lr_label_encoder = pickle.load(f) # deserialize using load()


def inference(image_file, label_encoder):
  """
  Fonction qui réalise une prédiction à partir d'un fichier image (ndarray ou PIL Image).
  """
  # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
  image_file_more_dims = np.expand_dims(image_file, axis=0)
  # Inférence
  pred = np.argmax(lr_classifier_restored.predict(image_file_more_dims), axis=1)[0]
  # Désencodage de l'index de classe en classe (string)
  pred_class_str = label_encoder.classes_[pred]
  # Retourne une string
  return pred_class_str



# Streamlit App
st.set_page_config(
  page_title="Reconnaissance d'iris",
  page_icon="👀",
  layout="centered"
)

# Header
st.header("Reconnaissance d'iris 👀", divider='rainbow')
st.markdown("Une applicaton pour la **reconnaissance d’oeil** pour authentifier vos employés.")
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
  st.image(image_pil)

  with st.spinner('Wait for it...'):
    lr_pred = inference(image_pil, lr_label_encoder)
  if lr_pred == 'left':
    st.success('Left!')
  elif lr_pred == 'right':
    st.success('Right!')

  # progress_text = "Operation in progress. Please wait."
  # my_bar = st.progress(0, text=progress_text)

  # for percent_complete in range(100):
  #   time.sleep(0.01)
  #   my_bar.progress(percent_complete + 1, text=progress_text)
  # time.sleep(1)
  # my_bar.empty()


