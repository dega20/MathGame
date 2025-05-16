from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.core.audio import SoundLoader  # Import SoundLoader to load music

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        # Background music (load it once)
        self.background_music = SoundLoader.load('sound/backsound1.mp3')
        if self.background_music:
            self.background_music.loop = True
            self.background_music.play()  # Start playing the music when the app launches

        # Background image
        bg_image = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        # FloatLayout to hold all widgets
        float_layout = FloatLayout()

        # Adding a semi-transparent overlay
        with float_layout.canvas.before:
            Color(0, 0, 0, 0.5)  # semi-transparent black
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        # Update rectangle size when window resizes
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Vertical BoxLayout for the content
        layout = BoxLayout(orientation='vertical', spacing=20, padding=[40, 100, 40, 100], 
                           size_hint=(0.8, 0.6), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Music volume slider with label
        layout.add_widget(Label(text="Volume Musik", font_size='24sp', color=(1, 1, 1, 1), 
                                size_hint=(1, 0.1)))
        self.music_volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(1, 0.1))
        self.music_volume_slider.bind(value=self.on_music_volume_change)  # Bind to volume change
        layout.add_widget(self.music_volume_slider)

        # Sound volume slider with label
        layout.add_widget(Label(text="Volume Suara", font_size='24sp', color=(1, 1, 1, 1), 
                                size_hint=(1, 0.1)))
        self.sound_volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(1, 0.1))
        layout.add_widget(self.sound_volume_slider)

        # Add layout to float layout
        float_layout.add_widget(layout)

        # Back button with custom icon
        back_button = Button(text="", size_hint=(None, None), size=(140, 140),
                             background_normal='img/back1.png',
                             background_down='img/back_icon_pressed.png',
                             pos_hint={'x': 0.01, 'top': 0.95})
        back_button.bind(on_release=self.go_back)
        float_layout.add_widget(back_button)

        # Adding everything to the screen
        self.add_widget(float_layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def on_music_volume_change(self, instance, value):
        # Update the background music volume based on the slider value
        if self.background_music:
            self.background_music.volume = value

    def go_back(self, instance):
        self.manager.current = 'menu'
