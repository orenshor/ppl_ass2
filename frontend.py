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

class MyGrid(FloatLayout):
    def openPopUp(self):
        show_res_popup()

class Popups(FloatLayout):
    pass

class ErrorPage(FloatLayout):
    pass

def show_res_popup():
    show = Popups()
    popupWindow = Popup(title="Popup Window", content=show,
                        size_hint=(None, None), size=(200, 200))
    popupWindow.open()

class MyApp(App):
    def build(self):
        self.UI = MyGrid()
        return self.UI

    def openPopUpSubmit(self):
        if(self.root.ids.count_res_input.text.isdigit() and len(self.root.ids.time_input.text) > 0 and len(self.root.ids.location_input.text) > 0):
            self.loc = self.root.ids.location_input.text
            self.duration = self.root.ids.time_input.text
            self.resCount = self.root.ids.count_res_input.text

            self.root.ids.location_input.text = ''
            self.root.ids.time_input.text = ''
            self.root.ids.count_res_input.text = ''
            self.UI.openPopUp()
        else:
            show = ErrorPage()
            self.popupWindowERR = Popup(title="OOPS!", content=show,
                                size_hint=(None, None), size=(400, 260))
            self.popupWindowERR.open()

    def closePopUp(self):
        self.popupWindowERR.dismiss()

if __name__ == "__main__":
    MyApp().run()
