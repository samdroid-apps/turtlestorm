import nxt
from nxt.motor import Motor
from nxt.sensor import Touch, Ultrasonic, Color20, Light, Type
from flask import Flask

MOTORS = {'A': nxt.PORT_A, 'B': nxt.PORT_B, 'C': nxt.PORT_C}
SENSORS = {'1': nxt.PORT_1, '2': nxt.PORT_2, '3': nxt.PORT_3, '4': nxt.PORT_4}
COLOR_NUMBER = {'red': Type.COLORRED, 'green': Type.COLORGREEN,
                'blue': Type.COLORBLUE, 'all': Type.COLORFULL,
                'none': Type.COLORNONE}
NUMBER_COLOR = {1: 'black', 2: 'blue', 3: 'green',
                4: 'yellow', 5: 'red', 6: 'white'}

app = Flask(__name__)
b = nxt.find_one_brick()

@app.after_request
def cross_domain(response):
    h = response.headers
    h['Access-Control-Allow-Origin'] = '*'
    h['Access-Control-Allow-Methods'] = 'GET, HEAD, OPTIONS'
    h['Access-Control-Max-Age'] = '0'
    return response

@app.route('/areyouarobot')
def are_you_a_robot():
    return 'yes'

@app.route('/about')
def about():
    return jsonify(motors=['A', 'B', 'C'], sensors=4)

@app.route('/motor/<letter>/start/<power>')
def motor_start(letter, power):
    m = Motor(b, MOTORS[letter.upper()])
    m.run(power=int(power))
    return 'OK'

@app.route('/motor/<letter>/stop')
def motor_stop(letter):
    m = Motor(b, MOTORS[letter.upper()])
    m.brake()
    return 'OK'

@app.route('/motor/<letter>/idle')
def motor_idle(letter):
    m = Motor(b, MOTORS[letter.upper()])
    m.idle()
    return 'OK'

@app.route('/motor/<letter>/turn/<deg>/<power>')
def motor_turn(letter, deg, power):
    m = Motor(b, MOTORS[letter.upper()])
    m.turn(int(power), int(deg))
    return 'OK'

@app.route('/touch/<port>')
def touch(port):
    t = Touch(b, SENSORS[port])
    return '1' if t.is_pressed() else '0'

@app.route('/ultrasonic/<port>')
def ultrasonic(port):
    u = Ultrasonic(b, SENSORS[port])
    return str(u.get_distance())

@app.route('/led/<port>/<color>')
def led(port, color):
    c = Color20(b, SENSORS[port])
    c.set_light_color(COLOR_NUMBER[color.lower()])
    return 'OK'

@app.route('/light/<port>')
def light(port):
    c = Color20(b, SENSORS[port])
    return str(c.get_light_color())

@app.route('/light/<port>/reflect/<color>')
def light_reflected(port, color):
    c = Color20(b, SENSORS[port])
    return str(c.get_reflected_light(COLOR_NUMBER[color.lower()]))

@app.route('/color/<port>')
def color(port):
    c = Color20(b, SENSORS[port])
    return str(c.get_color())

app.run(port=5002, debug=True, use_reloader=False)
