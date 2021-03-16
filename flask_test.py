from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

from pynput import keyboard

actual_state = 0

# inputs


def on_press(key):
    global actual_state
    actual_state = 1
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    global actual_state
    actual_state = 0
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# flask
app = Flask(__name__)


@app.route('/')
def index():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()
    return render_template('index.html')


@app.route('/state')
def state():
    global actual_state
    # actual_state += 1
    # if(actual_state > 2):
    #     actual_state = 0
    return str(actual_state)


if __name__ == '__main__':
    app.run(debug=True)
