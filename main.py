from flask import Flask, render_template, request
from NAV_API import NavAPI2

nav = NavAPI2("PRECONFIGURED")

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./controls.html')

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
app.run(host='0.0.0.0', port=5000, debug=True)
