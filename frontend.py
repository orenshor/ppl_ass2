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
        show_popup()
    pass

class Popups(FloatLayout):
    pass
def show_popup():
    print("user: ", ids.user_input.text)
    print("password: ", self.ids.password_input.text)
    show = Popups()
    popupWindow = Popup(title="Popup Window", content=show,
                        size_hint=(None, None), size=(200, 200))
    popupWindow.open()
class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
