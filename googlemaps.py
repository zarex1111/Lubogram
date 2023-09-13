from setup import *
import requests
from PIL import Image
import geocoder


def get_self_position():
    me = geocoder.ip("me")
    return me.latlng


def add_position_to_params(params, user_id=1, position=get_self_position()):
    if 'pt' in params:
        params['pt'] += '~'
    else:
        params['pt'] = ''
    params['pt'] += f'{position[1]},{position[0]},pmwtl{user_id}'
    return params
    

def get_image(center=get_self_position(), zoom="17", **params):
    params['apikey'] = API_KEY
    params['l'] = 'map'
    params['z'] = zoom
    params['ll'] = f'{center[1]},{center[0]}'
    params['lang'] = 'en_US'
    params = add_position_to_params(params)
    print(params)
    img = requests.get(STATIC_ADDRESS, params=params).content
    with open('result.png', 'wb') as file:
        file.write(img)
    im = Image.open('result.png')
    im.show()

if __name__ == '__main__':
    get_image()