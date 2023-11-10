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

# import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
# import keras


# Variables 
img_width = 320
img_height = 240
img_channels = 3
img_dim = (img_height, img_width, img_channels)

lr_classifier = "./models/lr_classifier.h5"
# id_left_classifier_path = "./models/lr_classifier.keras"

def check_file_exists(file_path):
  if os.path.exists(file_path):
    return True
  else:
    return False

print("LR CLassifier file exists : ", check_file_exists(lr_classifier))
# print("ID Left CLassifier file exists : ", check_file_exists(id_left_classifier_path))


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
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
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
  image_nd = np.array(image_pil)  
  image_nd_2 = np.array([image_nd])
  print(image_nd)
  print(image_nd.shape)
  print(image_nd_2.shape)

  # prediction
#   pred = [np.argmax(v) for v in lr_classifier.predict(np.array([image_nd]))]
#   st.write(pred)
#   label_enc_lr.classes_[y_test_pred_test][0]

#   pred_lr_enc = np.argmax(lr_classifier.predict(image_nd))
#   print(pred_lr_enc)


#   pred_lr = label_enc_lr.classes_[pred_lr_enc]
#   st.write(pred_lr)


