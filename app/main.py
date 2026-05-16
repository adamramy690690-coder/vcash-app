from kivy.app import App
from kivy.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import requests

class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(lambda x: setattr(self.manager, 'current', 'welcome'), 2)

class WelcomeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='v', padding=20, spacing=20)
        layout.add_widget(Label(text='VF CASH', font_size='32sp'))
        layout.add_widget(Button(text='Load', on_press=self.next))
        self.add_widget(layout)
    
    def next(self, *args):
        self.manager.current = 'verify'

class VerifyScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='v', padding=20, spacing=10)
        self.code = TextInput(hint_text='Code', multiline=False)
        layout.add_widget(self.code)
        layout.add_widget(Button(text='Verify', on_press=self.verify))
        self.add_widget(layout)
    
    def verify(self, *args):
        self.manager.current = 'main'

class MainScreen(Screen):
    pass

class VFCashApp(App):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(VerifyScreen(name='verify'))
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    VFCashApp().run()
