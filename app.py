import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from Adafruit_PWM_Servo_Driver import PWM
import math
import PlatformCalculator

kDegreesToRadians = (3.1415926535 / 180.0);
kXYLocations = [[0.0, 171.45], [-148.48, -85.725], [148.48, -85.725]];
pwm = PWM(0x40)


class MainScreen(GridLayout):

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.calc = PlatformCalculator.PlatformCalculator()
        self.calc.setSupportLocations(kXYLocations)

    def on_touch_down(self, touch):
        global firstTouchX
        global firstTouchY
        firstTouchX = touch.x
        firstTouchY = touch.y
        print('The first touch is at position', touch.pos)


    def on_touch_move(self, touch):
        zValues = [0.0, 0.0, 0.0]
        
        #self.calc.calculateSupportPositions(30.0, 83.2, zValues)
        #print(zValues[0])
        #print(zValues[1])
        #print(zValues[2])
        touchx = -1*(firstTouchX - touch.x)
        touchy = -1*(firstTouchY - touch.y)
        print('Pos compared to inital', touchx, " ", touchy)
        #if 'angle' in touch.profile:
        #    print('The touch angle is', touch.a)

class MyApp(App):

    def build(self):
        return MainScreen()

if __name__ == '__main__':
    MyApp().run()
