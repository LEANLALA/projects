from keys import *
from twython import TwythonStreamer
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(8,gpio.OUT)

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if "text" in data:
            print(data["text"])
            gpio.output(8,True)
            sleep(3)
            gpio.output(8,False)

    def on_error(self,status_code,data):
        print(status_code)

def searching_for_tweets():
    try:
        stream.statuses.filter(track="Madhup")
    except UnicodeEncodeError:
        searching_for_tweets()

stream=MyStreamer(API_key,API_key_secret,Access_token,Access_token_secret)
searching_for_tweets()
