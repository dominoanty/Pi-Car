import RPi.GPIO as GPIO
from time import sleep


class NavAPI:
    def __init__(self, CONFIG="MANUAL"):
        if(CONFIG=="PRECONFIGURED"):
            self.set_left_motor_inputs()
            self.set_left_motor_enable()
            self.set_right_motor_inputs()
            self.set_right_motor_enable()
            self.registerGPIO()
    
    def set_left_motor_inputs(self, lt_frd=03, lt_bck=05):
        self.lt_frd = lt_frd
        self.lt_bck = lt_bck

    def set_left_motor_enable(self, lt_en=07):
        self.lt_en = lt_en
        self.lt_pwm = GPIO.PWM(self.lt_en, 100)

    def set_right_motor_inputs(self, rt_frd=36, rt_bck=38):
        self.rt_frd = rt_frd
        self.rt_bck = rt_bck

    def set_right_motor_enable(self, rt_en=40):
        self.rt_en = rt_en
        self.rt_pwm = GPIO.PWM(self.rt_en, 100)

    def registerGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.lt_frd, GPIO.OUT)
        GPIO.setup(self.lt_bck, GPIO.OUT)
        GPIO.setup(self.lt_en, GPIO.OUT)
        GPIO.setup(self.rt_frd, GPIO.OUT)
        GPIO.setup(self.rt_bck, GPIO.OUT)
        GPIO.setup(self.rt_en, GPIO.OUT)
        self.lt_pwm.start(0)
        self.rt_pwm.start(0)

    def disableAllInputs(self):
        GPIO.output(self.lt_en, False)
        GPIO.output(self.rt_en, False)

    def enableAllInputs(self):
        GPIO.output(self.lt_en, True)
        GPIO.output(self.rt_en, True)


    
    def move_forward(self, TIME=1, THROTTLE=100):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, True)
        GPIO.output(self.rt_frd, True)
        GPIO.output(self.lt_bck, False)
        GPIO.output(self.rt_bck, False)
        self.lt_pwm.ChangeDutyCycle(THROTTLE)
        self.rt_pwm.ChangeDutyCycle(THROTTLE)
        self.enableAllInputs()
        sleep(TIME)

    def move_backward(self, TIME=1, THROTTLE=50):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, False)
        GPIO.output(self.rt_frd, False)
        GPIO.output(self.lt_bck, True)
        GPIO.output(self.rt_bck, True)
        self.lt_pwm.ChangeDutyCycle(THROTTLE)
        self.rt_pwm.ChangeDutyCycle(THROTTLE)
        self.enableAllInputs()
        sleep(TIME)


    def move_left_forward(self, TIME=1, THROTTLE=50):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, False)
        GPIO.output(self.rt_frd, True)
        GPIO.output(self.lt_bck, False)
        GPIO.output(self.rt_bck, False)
        self.lt_pwm.ChangeDutyCycle(0)
        self.rt_pwm.ChangeDutyCycle(THROTTLE)
        self.enableAllInputs()
        sleep(TIME)

    def move_left_backward(self, TIME=1, THROTTLE=50):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, False)
        GPIO.output(self.rt_frd, False)
        GPIO.output(self.lt_bck, False)
        GPIO.output(self.rt_bck, True)
        self.lt_pwm.ChangeDutyCycle(0)
        self.rt_pwm.ChangeDutyCycle(THROTTLE)
        self.enableAllInputs()
        sleep(TIME)
    
    def move_right_forward(self, TIME=1, THROTTLE=50):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, True)
        GPIO.output(self.rt_frd, False)
        GPIO.output(self.lt_bck, False)
        GPIO.output(self.rt_bck, False)
        self.lt_pwm.ChangeDutyCycle(THROTTLE)
        self.rt_pwm.ChangeDutyCycle(0)
        self.enableAllInputs()
        sleep(TIME)

    def move_right_backward(self, TIME=1, THROTTLE=50):
        self.disableAllInputs()
        GPIO.output(self.lt_frd, False)
        GPIO.output(self.rt_frd, False)
        GPIO.output(self.lt_bck, True)
        GPIO.output(self.rt_bck, False)
        self.lt_pwm.ChangeDutyCycle(THROTTLE)
        self.rt_pwm.ChangeDutyCycle(0)
        self.enableAllInputs()
        sleep(TIME)

    def stop(self):
        self.disableAllInputs()
        self.lt_pwm.stop()
        self.rt_pwm.stop()
        GPIO.cleanup()

        






