from keras.models import load_model
import numpy as np
import cv2

def image_to_feature_vector(image, size=(32, 32)):
	return cv2.resize(image, size).flatten()

classes = ["cancer", "no_cancer"]

model = load_model("unidad/Colaboratory/output/try1.hdf5")

image = cv2.imread("unidad/Colaboratory/test_cancer/1.png")

features = image_to_feature_vector(image) / 255.0

features = np.array([features])

probs = model.predict(features)[0]
prediction = probs.argmax(axis=0)

label = "{}: {:.2f}%".format(classes[prediction], probs[prediction] * 100)
print("Classification and probability = {}".format(label))