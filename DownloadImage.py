import requests


def download(url='', name=''):
    destination_path = 'Assert/'+name+'.jpg'
    print('Trying to download image...')
    with open(destination_path, 'wb') as handle:
        response = requests.get(url, stream=True)
        if not response.ok:
            print('Failed to download image. :(')
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
        print('Image downloaded! :D')