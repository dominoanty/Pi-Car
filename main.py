from picamera import PiCamera
from flask import Flask, render_template, request
from DummyNAV import DummyNAV
from lane_detector import get_lane_angle
import time
THRESH = 12


camera = PiCamera()
camera.resolution = (240,180)
camera.framerate = 10
camera.color_effects = (128, 128)


try:
    from NAV_API import NavAPI2
    nav = NavAPI2("PRECONFIGURED")
except RuntimeError:
    nav = DummyNAV()

def min_max_normalizer(old_max, old_min, new_max, new_min):
    def inner_func(x):
        if x > old_max:
            return new_max
        return float(new_min) + float(x - old_min)/(old_max - old_min)*float(new_max-new_min)
    return inner_func

min_max = min_max_normalizer(0, 45, 0, 1)



app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./controls.html')

@app.route('/move', methods = ['POST'])
def move():
    angle = get_lane_angle(camera)
    dir = ""
    if(abs(angle)<THRESH):
        move_forward()
        dir = "forward"
    elif(angle>0):
        move_forward_left()
        dir = "left"
    else:
        move_forward_right()
        dir = "right"
    time.sleep(0.05)
    move_dummy()
    return "moved. ha "+dir+ " "+str(angle)

@app.route('/move/forward', methods = ['POST'])
def move_forward():
    nav.move_forward()
    return 'Moving forward in direction '


@app.route('/move/backward', methods = ['POST'])
def move_backward():
    nav.move_backward()
    return 'Moving backward in direction '

@app.route('/move/left', methods=['POST'])
def move_left():
    return 'Moving left'

@app.route('/move/right', methods=['POST'])
def move_right():
    return 'Moving right'

@app.route('/move/forward_left', methods=['POST'])
def move_forward_left():
    nav.move_left_forward()
    return 'Moving forward left'

@app.route('/move/forward_right', methods=['POST'])
def move_forward_right():
    nav.move_right_forward()
    return 'Moving forward_right'

@app.route('/move/backward_left', methods=['POST'])
def move_backward_left():
    nav.move_left_backward()
    return 'Moving backward_left'

@app.route('/move/backward_right', methods=['POST'])
def move_backward_right():
    nav.move_right_backward()
    return 'Moving backward right'

@app.route('/move/dummy', methods=['POST'])
def move_dummy():
    nav.stop()
    return 'dummy'

app.debug = True
app.run(host='0.0.0.0', port=5000, debug=False)
