from flask import Flask, render_template, request
# from picar.nav_api import NavAPI
# NAPI = NavAPI()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('./controls.html')

@app.route('/move/forward', methods = ['POST'])
def move_forward():
    print(request.form)
    direction = request.form['direction']
    if direction is None:
        direction = 'None'
    return 'Moving forward in direction ' + direction


@app.route('/move/backward', methods = ['POST'])
def move_backward():
    direction = request.form['direction']
    if direction is None:
        direction = 'None'
    return 'Moving backward in direction ' + direction

@app.route('/move/left', methods=['POST'])
def move_left():
    return 'Moving left'

@app.route('/move/right', methods=['POST'])
def move_right():
    return 'Moving right'


app.debug = True
app.run()