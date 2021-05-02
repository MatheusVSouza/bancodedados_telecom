import os
import requests
from flask import Flask, Response, request, render_template
from pynput.keyboard import Key, Controller
keyboard = Controller()        
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html"), 200

@app.route("/videocontrol/shutdown/<second>")
def shutdown(second):
    str_aux1 = "shutdown /s "
    str_aux2 = "/t %s" %second
    st = str_aux1 + str_aux2
    os.system(st)
    return render_template("index.html"), 200

@app.route("/videocontrol/cancelshutdown")
def cancel_shutdown():
    os.system("shutdown -a")
    return render_template("index.html"), 200


@app.route("/videocontrol/volumeup")
def control_volume_up():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    return render_template("index.html"), 200

@app.route("/videocontrol/volumedown")
def control_volume_down():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    return render_template("index.html"), 200

@app.route("/videocontrol/pause")
def video_pause():
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    return render_template("index.html"), 200

@app.route("/videocontrol/fullscreen")
def fullscreen():
    keyboard.press('f')
    keyboard.release('f')
    return render_template("index.html"), 200

@app.route("/videocontrol/foward")
def foward():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    return render_template("index.html"), 200

@app.route("/videocontrol/backward")
def backward():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    return render_template("index.html"), 200

@app.route("/videocontrol/next")
def next():
    keyboard.press(Key.shift)
    keyboard.press('n')
    keyboard.release('n')
    keyboard.release(Key.shift)
    return render_template("index.html"), 200

if  __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")