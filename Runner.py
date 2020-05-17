#  Ref : https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826

from DetectFace import detect_face
from DownloadImage import download
from RecogniseFace import recognise_face
from TrainingFace import Training

if __name__ == '__main__':
    # URL = input('Enter image url to download\n')
    print('Start of application,')

    # URL = 'https://www.androidpolice.com/wp-content/uploads/2019/05/c7e98610gy1g336go41ipj21111jktf0-1.jpg'
    # download(url=URL,name='original')
    # file_path = 'Assert/original.jpg'
    # detect_face(image_path=file_path,name='original')

    # Training(image_path=file_path)

    # URL = 'https://www.androidpolice.com/wp-content/uploads/2020/04/OnePlus-8-Series-Ft.-Robert-Downey-Jr.-Official-Promotional-Video-With-Action-and-Fun-0001.png'
    # download(url=URL,name='reference')
    # file_path = 'Assert/reference.jpg'
    # detect_face(image_path=file_path,name='reference')

    recognise_face(image_path='Assert/reference_detected.jpg')





