from Adafruit_PWM_Servo_Driver import PWM
import time
import math
##Tick Range 420 @ 50Hz
##Servo Center at 390
pwm=PWM(0x40)
Arm1Length=3.48
Arm2Length=3.48
Arm3Length=2.77
def PositionServo(Channel, Angle):
  PWMFrequency=50
  pwm.setPWMFreq(PWMFrequency)
  Angle0=[155,122,95]
  Angle180=[530,545,525]
  ZeroValue=[530,337,306.5]
  if Channel != 0:
    Angle=-Angle    
  TicksPerAngle=(Angle180[Channel]-Angle0[Channel])/180
  TickValue=int(ZeroValue[Channel]-TicksPerAngle*Angle)
  pwm.setPWM(Channel,0,TickValue)


def ArmPosition(Xe,Ye,ThetaE,Comment):
  ThetaE=ThetaE*3.14159/180
  X2=Xe-Arm3Length*math.sin(ThetaE)
  Y2=Ye+Arm3Length*math.cos(ThetaE)
  A=math.sqrt(X2**2+Y2**2)
  Theta2=3.14159-math.acos((Arm1Length**2+Arm2Length**2-A**2)/(2*Arm1Length*Arm2Length))
  ThetaB=math.atan2(Y2,X2)
  ThetaA=math.acos((Arm1Length**2+A**2-Arm2Length**2)/(2*Arm1Length*A))
  Theta1=ThetaA+ThetaB
  Theta3=3.14159/2-ThetaE+Theta1-Theta2

  PositionServo(0,Theta1*180/3.14159)
  PositionServo(1,Theta2*180/3.14159)
  PositionServo(2,Theta3*180/3.14159)


  if (Comment==1):
    X2=Arm1Length*math.cos(Theta1)
    Y2=Arm1Length*math.sin(Theta1)
    X3=X2+Arm2Length*math.cos(Theta2-Theta1)
    Y3=Y2-Arm2Length*math.sin(Theta2-Theta1)
    Xe=X3+Arm3Length*math.cos(Theta2-Theta1+Theta3)
    Ye=Y3-Arm3Length*math.sin(Theta2-Theta1+Theta3)
    ThetaE=(3.14159/2-Theta3-Theta2+Theta1)*180/3.14159
    print("Xe=",Xe)
    print("Ye=",Ye)
    print("ThetaE=",ThetaE)
    print ("X1=",X2, "X2=", Y2)
    print ("A=", A, "ThetaB=",ThetaB, "ThetaA=",ThetaA)
    print ("Theta1=", Theta1*180/3.14159)
    print ("Theta2=", Theta2*180/3.14159)
    print ("Theta3=", Theta3*180/3.14159)

  
for Xe in range(200,275):
  ArmPosition(Xe/50,0,0,0)
  
ArmPosition(5,1,90,0)
time.sleep(.5)
for Ye in range(25,275):
  ArmPosition(7,Ye/50,90,0)

for Xe in range(0,400):
  ArmPosition(5-Xe/50,7,180,0)


