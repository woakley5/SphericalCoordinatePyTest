from Adafruit_PWM_Servo_Driver import PWM
import time

pwm=PWM(0x40)

def PositionServo(Channel, Angle):
  PWMFrequency=50
  pwm.setPWMFreq(PWMFrequency)
  Angle0=[100,122,0]
  Angle180=[530,545,525]
  ZeroValue=[530,337,100]
  if Channel != 0:
    Angle=-Angle    
  TicksPerAngle=(Angle180[Channel]-Angle0[Channel])/180
  TickValue=int(ZeroValue[Channel]-TicksPerAngle*Angle)
  print(TickValue)
  pwm.setPWM(Channel,0,TickValue)

PositionServo(0, 0)
PositionServo(1, 0)
PositionServo(2, 0)

time.sleep(2)
PositionServo(0, 180)
PositionServo(1, 180)
PositionServo(2, 180)
