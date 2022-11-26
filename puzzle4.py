# from keras.models import load_model
#
# model = load_model('model.hdf5')
# layers = model.layers
# for x in layers:
#     print(x)

# from keras.models import load_model

# model = load_model('model.hdf5')
# layers = model.layers
# for x in layers:
#     print(x)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import jwt

import os
import requests


def start_driver():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = { 'browser':'ALL' }
    driver = webdriver.Chrome(desired_capabilities=d)
    driver.get('https://hotsinglebots.delorean.codes/u/spencerc99/find')
    # for name in ['browser', 'driver', 'server']:
        # print driver.get_log(name)
    time.sleep(1)
    driver.execute_script("window.open('https://hotsinglebots.delorean.codes/u/spencerc99/profile');")
    driver.get('https://hotsinglebots.delorean.codes/u/spencerc99/profile')
    # print('josh is a loser.')
    return driver

def process_match(driver):
    preference = driver.execute_script("return jwt_decode(localStorage.currentBot).preference.label;")
    print (preference)

    # actions = ActionChains(driver)

    # actions.key_down(Keys.COMMAND + "T").key_up(Keys.COMMAND + "T").perform()
    time.sleep(1)

import base64
def js_to_run(im):
    arr = 'data:image/jpg;base64,'
    f = open(im + '.jpg', 'rb')
    enc = base64.b64encode(f.read())
    return 'localStorage.profilePicture='

IMG = 'https://hotsinglebots.delorean.codes/api_predict/jacobj10/predict'
os.chdir('puzzle4images')
name = "ship"
files = {'image': open(name+ '.jpg', 'rb')}
resp = requests.post(IMG, files=files)

# print resp

if __name__ == '__main__':
    driver = start_driver()
    process_match(driver)
