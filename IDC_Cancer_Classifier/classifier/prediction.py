from keras.models import load_model
from flask import current_app
import numpy as np
import cv2
import os


def image_to_feature_vector(image, size=(32, 32)):
    return cv2.resize(image, size).flatten()


def predict():
    classes = ["cancer", "no_cancer"]

    model = load_model(os.path.join(current_app.root_path, 'classifier', 'model', 'idc_model.hdf5'))

    image = cv2.imread(os.path.join(current_app.root_path, 'classifier', 'test_cancer', '1.no_cancer.png'))

    features = image_to_feature_vector(image) / 255.0

    features = np.array([features])

    probs = model.predict(features)[0]
    prediction = probs.argmax(axis=0)

    label = "{}: {:.2f}%".format(classes[prediction], probs[prediction] * 100)
    print("Classification and probability = {}".format(label))
