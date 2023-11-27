from pyfirmata import Arduino, SERVO

port='COM4'

pin=10

board=Arduino(port)

board.digital[pin].mode=SERVO

def servoMove(pin, angle):
    board.digital[pin].write(angle)

def doorMove(val):
    if val=="Mask":
        servoMove(pin, 40)
    elif val=="No Mask":
        servoMove(pin, 180)



        
   
