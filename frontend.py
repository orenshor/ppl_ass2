import ctypes

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import kivy
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.popup import Popup
import mybackend

class MyGrid(FloatLayout): pass

class ErrorPage(FloatLayout): pass

class MyApp(App):

    def build(self):
        return MyGrid()
    ## function that actiave when click on Let's Go button. make all the inputs checks and activate the backend
    def openPopUpSubmit(self):
        if(self.root.ids.count_res_input.text.isdigit() and self.root.ids.time_input.text.isdigit() and  len(self.root.ids.location_input.text) > 0):
            self.loc = self.root.ids.location_input.text
            self.duration = self.root.ids.time_input.text
            self.resCount = self.root.ids.count_res_input.text

            self.root.ids.location_input.text = ''
            self.root.ids.time_input.text = ''
            self.root.ids.count_res_input.text = ''
            try:
                #BackEnd:calculate the answer
                db = mybackend.Database()
                answers =db.calculate_recommendations(self.loc,int(self.duration), int(self.resCount))
                self.popupWindowSuccess = Popup(title="Results Window", content=Label(text=str('\n'.join(answers)), halign='center'),
                                                size_hint=(None, None), size=(400, 300)).open()
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(0, e.args[0], u"Error",  0)


        else:
            self.popupWindowERR = Popup(title="OOPS!", content=ErrorPage(),
                                size_hint=(None, None), size=(400, 260))
            self.popupWindowERR.open()

    # function that close the Error popUp
    def closePopUpERR(self):
        self.popupWindowERR.dismiss()


if __name__ == "__main__":
    MyApp().run()
