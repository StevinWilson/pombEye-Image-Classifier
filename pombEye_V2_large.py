# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image


import numpy as np
import os
from numpy import ndarray
import cv2
import sys


tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0 :
    config = tf.config.experimental.set_memory_growth(physical_devices[0], True)

model = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), 'pombEye_xception.h5'))

categories = {'Cytosol': 0,
'Cytosol and Nucleus': 1,
'Endoplasmic reticulum': 2,
'Punctate (or Golgi Apparatus)': 3,
'Microtubules': 4,
'Mitochondrion': 5,
'Nucleus': 6,
'Periphery': 7,
'Vacuole': 8}

print("Thank you for using pombEye V2-large")

print("Type 'exit' to quit pombEye")


while True:
    filename = input("Enter file path: ")
    filename = str(filename)
    filename = filename.rstrip()
    if filename == 'exit':
        break
    try:
        assert os.path.exists(filename), "File not found at, "+str(filename)
        img = cv2.imread(filename,0)
        cv2.imwrite('temp.jpg',img)
        test_image = image.load_img(os.path.join(os.path.dirname(__file__),'temp.jpg'), target_size = (299, 299))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        test_image = test_image.astype("float") / 255.0
        result = model.predict(test_image)
        print("\n\n")
        print("Input converted to grayscale and saved as temp.jpg in the working directory")
        print("\n")
        print("Predicted localisation")
        print("Prediction", " : ", "Confidence score (Max value = 100)")
        for classes, number in categories.items():
            if number == result.argmax():
                print(classes, " : ", round(np.amax(result)*100,2),"\n\n")
        for classes, number in categories.items():
            print(classes, " " , round(result.item(number)*100,2))
        print("\n\n")
        continue
    except:
        print("Not a valid input")
        continue
