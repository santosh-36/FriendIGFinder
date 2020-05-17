import cv2
import numpy as np
from PIL import Image
import os


def Training(image_path=''):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    print('Training faces. It will take a few seconds. Wait ...')

    # t = [os.path.join('Assert', f) for f in os.listdir('Assert')]
    imagePaths = [image_path]
    faceSamples, ids = [], []

    count = 0
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        # id =  int(os.path.split(imagePath)[-1].split(".")[1])
        id = count
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y + h, x:x + w])
            ids.append(id)
        count += 1
    recognizer.train(faceSamples, np.array(ids))

    recognizer.write('Assert/trainer.yml')
    print("{0} face(s) trained.".format(len(np.unique(ids))))