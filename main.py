from flask import Flask, render_template, request
# from picar.nav_api import NavAPI
# NAPI = NavAPI()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./controls.html')

@app.route('/move/forward', methods = ['POST'])
def move_forward():
    return 'Moving forward in direction ' 


@app.route('/move/backward', methods = ['POST'])
def move_backward():
    return 'Moving backward in direction '

@app.route('/move/left', methods=['POST'])
def move_left():
    return 'Moving left'

@app.route('/move/right', methods=['POST'])
def move_right():
    return 'Moving right'

@app.route('/move/forward_left', methods=['POST'])
def move_forward_left():
    return 'Moving forward left'

@app.route('/move/forward_right', methods=['POST'])
def move_forward_right():
    return 'Moving forward_right'

@app.route('/move/backward_left', methods=['POST'])
def move_backward_left():
    return 'Moving backward_left'

@app.route('/move/backward_right', methods=['POST'])
def move_backward_right():
    return 'Moving backward right'

@app.route('/move/dummy', methods=['POST'])
def move_dummy():
    return 'dummy'

app.debug = True
app.run()