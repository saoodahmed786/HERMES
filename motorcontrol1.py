import RPi.GPIO as GPIO          
from time import sleep


#assign GPIO pin# to outgoing direction and PMW signals
in1 = 24
in2 = 23
en = 25
temp1=1

m1 = 5
m2 = 6
pmw_1 = 13 
pwm_2 = 19
 

# setup the GPIO pins to outgoing
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(pmw_1, GPIO.OUT)
GPIO.setup(pmw_2, GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(m1, GPIO.LOW)
GPIO.output(m2, GPIO.LOW)


#set frequency of PWM
p=GPIO.PWM(en,1000)
p1=GPIO.PWM(pwm_1,1000)
p2=GPIO.PWM(pwm_2,1000)

# GPIO.high spins motor counter clockwise 
# GPIO.LOW spins the motor clockwise


""" 
forward direction, m1 spins counterclockwise, m2 spins clockwise
backward direction, m1 spins clockwise, m2 spins counter clockwise
turn left, m1 spins clockwise, m2 spins clockwise
turn right, m1 spins counter , m2 spins counter """ 


#start PWM at what duty cycle
p.start(25)
p1.start(0)
p2.start(0)


print("\n")
print("The default speed & direction of motor is 0 & Forward.....")
x = input("r-run s-stop f-forward b-backward l-low m-medium  h-high e-exit")
x = input("r-run, w-forward, s-backward, a-turn left, d-turn right,l-low, m-medium, h-high, e-exit")
print("\n")    


while(1):

    x = input()
    
    if x == 'r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
	 GPIO.output(m1,GPIO.HIGH)
         GPIO.output(m2,GPIO.LOW)

         print("forward")
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
	 GPIO.output(m1,GPIO.LOW)
         GPIO.output(m2,GPIO.HIGH)
         print("backward")

    elif x == 's':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        p.ChangeDutyCycle(0)
        p1.ChangeDutyCycle(0)
        p2.ChangeDutyCycle(0)

        
    elif x == 'w':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
	GPIO.output(m1,GPIO.HIGH)
	GPIO.output(m2,GPIO.LOW)
        temp1=1

    elif x == 'f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
	temp1=1


    elif x == 's':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
	GPIO.output(m1,GPIO.LOW)
        GPIO.output(m2,GPIO.HIGH)
        temp1=0

    elif x == 'b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
	
    elif x == 'a':
        print("turn left")
	GPIO.output(m1,GPIO.LOW)
        GPIO.output(m2,GPIO.LOW)
        temp1=0

    elif x == 'd':
        print("turn right")
	GPIO.output(m1,GPIO.HIGH)
        GPIO.output(m2,GPIO.HIGH)
        temp1=0


    elif x == 'l':
        print("low")
        p.ChangeDutyCycle(25)
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)

    elif x == 'm':
        print("medium")
        p.ChangeDutyCycle(50)
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)


    elif x == 'h':
        print("high")
        p.ChangeDutyCycle(75)
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)

     
    
    elif x == 'e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        break

