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

class SuccessPage(FloatLayout): pass

class ErrorPage(FloatLayout): pass

class MyApp(App):
    def build(self):
        return MyGrid()

    def openPopUpSubmit(self):
        if(self.root.ids.count_res_input.text.isdigit() and self.root.ids.time_input.text.isdigit() and  len(self.root.ids.location_input.text) > 0):
            self.loc = self.root.ids.location_input.text
            self.duration = self.root.ids.time_input.text
            self.resCount = self.root.ids.count_res_input.text

            self.root.ids.location_input.text = ''
            self.root.ids.time_input.text = ''
            self.root.ids.count_res_input.text = ''
            self.popupWindowSuccess = Popup(title="Results Window", content=SuccessPage(),
                                size_hint=(None, None), size=(200, 200))
            self.popupWindowSuccess.open()
            ## calculate the answer - return in DataFrame
            db = mybackend.Database()
            self.answers = db.calculate_recommendations(self.loc,self.duration,self.resCount)


        else:
            self.popupWindowERR = Popup(title="OOPS!", content=ErrorPage(),
                                size_hint=(None, None), size=(400, 260))
            self.popupWindowERR.open()

    def closePopUpERR(self):
        self.popupWindowERR.dismiss()

    def closePopUpSuccess(self):
        self.popupWindowSuccess.dismiss()


if __name__ == "__main__":
    MyApp().run()
