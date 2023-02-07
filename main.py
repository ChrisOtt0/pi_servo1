import RPi.GPIO as gpio
servo_pin = 21
gpio.setmode(gpio.BCM)
gpio.setup(servo_pin, gpio.OUT)
pwm_servo = gpio.PWM(servo_pin, 50)
pwm_servo.start(5)

while True:
    d = input("Enter % or 'quit' to exit: ")
    if d == "quit":
        break

    duty = int(d)
    pwm_servo.ChangeDutyCycle(duty)

gpio.cleanup()
