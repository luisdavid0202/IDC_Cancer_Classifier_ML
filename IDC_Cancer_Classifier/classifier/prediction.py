from keras.models import load_model
# TODO: quitar la dependencia de flask y de os de este script
from flask import current_app
import numpy as np
from keras import backend as K
import cv2
import os


def image_to_feature_vector(image, size=(32, 32)):
    return cv2.resize(image, size).flatten()


def predict(image_path):
    classes = ["cancer", "no_cancer"]

    model = load_model(os.path.join(current_app.root_path, 'classifier', 'model', 'idc_model.hdf5'))
    image = cv2.imread(image_path)
    features = image_to_feature_vector(image) / 255.0
    features = np.array([features])
    probs = model.predict(features)[0]
    prediction = probs.argmax(axis=0)

    label = "{}: {:.2f}%".format(classes[prediction], probs[prediction] * 100)
    K.clear_session()
    return "Classification and probability = {}".format(label)
