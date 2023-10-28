import streamlit as st
import pandas as pd
import numpy as np
# import tensorflow as tf
from PIL import Image

# import cv2

import os
import random
import datetime
import shutil


# Variables 
img_width = 320
img_height = 240
img_channels = 3
img_dim = (img_height, img_width, img_channels)

lr_classifier = "./models/lr_classifier.keras"
id_left_classifier_path = "./models/lr_classifier.keras"


def check_file_exists(file_path):
  if os.path.exists(file_path):
    return True
  else:
    return False

print("LR CLassifier file exists : ", check_file_exists(lr_classifier))
print("ID Left CLassifier file exists : ", check_file_exists(id_left_classifier_path))


# # Importer le modèle 'LR Classifier'
# lr_classifier_loaded = tf.keras.models.load_model(lr_classifier_path)
# lr_classifier.summary()



# # Importer le label encoder
# # 'rb' = read binary
# with open(lr_label_encoder_path, 'rb') as f:
#   label_enc_lr_loaded = pickle.load(f) # deserialize using load()
# print(label_enc_lr_loaded.classes_)


# # Load models
# from tensorflow.keras.models import load_model
# lstm_model = load_model('./models/BiLstm_model.h5')
# # Importer le modèle 'LR Classifier'
# lr_classifier_loaded = tf.keras.models.load_model(lr_classifier_path_keras)
# lr_classifier.summary()









# def lr_inference(image_file):
#   """
#   Fonction qui réalise une prédiction à partir d'un fichier image (ndarray ou PIL Image).
#   """
#   # Ajout d'une dimension car le modèle accepte une liste d'images cad un objet à 4 dimensions.
#   image_file_more_dims = np.expand_dims(image_file, axis=0)
#   # Inférence
#   pred = [np.argmax(v) for v in id_left_classifier_loaded.predict(image_file_more_dims)][0]
#   # Retourne une string
#   return pred