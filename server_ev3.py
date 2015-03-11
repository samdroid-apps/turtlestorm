from ev3.ev3dev import Motor
from ev3.lego import TouchSensor, ColorSensor, UltrasonicSensor, GyroSensor
from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/motor/<letter>/start/<int:power>')
def motor_start(letter, power):
    # m = Motor(Motor.PORTS.__getattr__(letter.upper()))
    # Hope just using the letter works
    m = Motor(letter.upper())
    m.run_forever(power, regulation_mode=False)
    return 'OK'

@app.route('/motor/<letter>/stop')
def motor_stop(letter):
    m = Motor(letter.upper())
    m.stop_mode = Motor.STOP_MODE.BRAKE  # Maybe HOLD?
    m.stop()
    return 'OK'

@app.route('/motor/<letter>/idle')
def motor_idle(letter):
    m = Motor(letter.upper())
    m.stop_mode = Motor.STOP_MODE.COAST
    m.stop()
    return 'OK'

@app.route('/motor/<letter>/turn/<int:deg>/<int:power>')
def motor_turn(letter, deg, power):
    m = Motor(letter.upper())
    # I don't think the api resets the position to base measurements off?
    m.run_position_limited(deg, power, position=0)
    return 'OK'

@app.route('/touch/<int:port>')
def touch(port):
    t = TouchSensor(port)
    return '1' if t.is_pushed else '0'

@app.route('/ultrasonic/<int:port>')
def ultrasonic(port):
    u = UltrasonicSensor(port)
    return str(u.dist_cm)

# I don't think the ev3 can do this
@app.route('/led/<int:port>/<color>')
def led(port, color):
    return 'IDK'

@app.route('/light/<int:port>')
def light(port):
    c = ColorSensor(port)
    return str(c.ambient)

# You only get red light with ev3
@app.route('/light/<int:port>/reflect/<color>')
def light_reflected(port, color):
    c = ColorSensor(port)
    return str(c.reflect)

@app.route('/color/<int:port>')
def color(port):
    c = ColorSensor(port)
    return str(c.color)

@app.route('/gyro/angle/<int:port>')
def gyro_angle(port):
    g = GyroSensor(port)
    return str(g.ang)

@app.route('/gyro/rate/<int:port>')
def gyro_rate(port):
    g = GyroSensor(rate)
    return str(g.rate)

app.run(port=5002, debug=True, use_reloader=False)
