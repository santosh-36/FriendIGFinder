import cv2


def detect_face(image_path='', name=''):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )
    print('{0} faces found.'.format(len(faces)))
    count = 0
    for(x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roiColor = image[y:y+h, x:x+w]
        cv2.imwrite('Assert/'+name+'_{0}.jpg'.format(count), image)
        count += 1
    if cv2.imwrite('Assert/'+name+'_detected.jpg', roiColor):
        print('Detected Successfully.')
    else:
        print('Detection Failed.')