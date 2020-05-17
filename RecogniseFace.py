import cv2


def recognise_face(image_path=''):
    print('Recognising face...\n')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Assert/trainer.yml')
    id, confidence = recognizer.predict(gray)
    # Check if confidence is less than 100 ==> "0" is perfect match
    matchPercentage = 100 - confidence
    # change 20 accordingly
    if matchPercentage < 20:
        print('Matched')
    else:
        print('Un-match')
