from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.app import App

class PilihScreen(Screen):
    def __init__(self, **kwargs):
        super(PilihScreen, self).__init__(**kwargs)
        
        # Layout to hold buttons and background
        self.float_layout = FloatLayout()

        # Background image for the main screen
        background = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.float_layout.add_widget(background)

        # First button with background image
        self.button1 = Button(text="", size_hint=(0.4, 0.2),
                              pos_hint={'center_x': 0.3, 'center_y': 0.5},
                              background_normal='img/hafal.png',  # Image for button
                              background_down='img/button1_pressed.png')
        self.button1.bind(on_release=self.show_popup)
        self.float_layout.add_widget(self.button1)

        # Second button with background image
        self.button2 = Button(text="", size_hint=(0.4, 0.2),
                              pos_hint={'center_x': 0.7, 'center_y': 0.5},
                              background_normal='img/kuis.png',  # Image for button
                              background_down='img/button2_pressed.png')
        self.button2.bind(on_release=self.show_popup)
        self.float_layout.add_widget(self.button2)

        self.add_widget(self.float_layout)

    def show_popup(self, instance):
        # Popup layout
        popup_layout = FloatLayout()

        # Popup background image
        popup_background = Image(source='img/popup_bg.png', allow_stretch=True, keep_ratio=False)
        popup_layout.add_widget(popup_background)

        # First button inside popup with background image
        popup_button1 = Button(text="", size_hint=(0.4, 0.2),
                               pos_hint={'center_x': 0.3, 'center_y': 0.5},
                               background_normal='img/popup_button1.png',  # Image for popup button
                               background_down='img/popup_button1_pressed.png')
        popup_button1.bind(on_release=lambda x: self.go_to_screen('page1'))
        popup_layout.add_widget(popup_button1)

        # Second button inside popup with background image
        popup_button2 = Button(text="", size_hint=(0.4, 0.2),
                               pos_hint={'center_x': 0.7, 'center_y': 0.5},
                               background_normal='img/popup_button2.png',  # Image for popup button
                               background_down='img/popup_button2_pressed.png')
        popup_button2.bind(on_release=lambda x: self.go_to_screen('page2'))
        popup_layout.add_widget(popup_button2)

        # Create and open popup with background image
        popup = Popup(title='Select Page', content=popup_layout, size_hint=(0.8, 0.4),
                      background='img/popup_frame.png')  # Background for the popup frame
        popup.open()

    def go_to_screen(self, screen_name):
        # Navigate to other screens
        self.manager.current = screen_name
