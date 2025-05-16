from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.app import App
from kivy.animation import Animation
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import PushMatrix, PopMatrix, Rotate

class MenuScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        app.play_menu_music()

        self.animate_widgets()

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.float_layout = FloatLayout()

        # Background Image
        background = Image(source='img/bg1.png', allow_stretch=True, keep_ratio=False)
        self.float_layout.add_widget(background)

        # Title Layout
        self.title_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.3), pos_hint={'center_x': 0.5, 'center_y': 1.5})
        self.title = Image(source='img/text1.png')
        self.title_layout.add_widget(self.title)
        self.float_layout.add_widget(self.title_layout)

        # Animal Image Behind Buttons
        self.animal_image = Image(source='img/panda.png', size_hint=(None, None), size=(1200, 360),
                                  pos_hint={'center_x': 0.5, 'center_y': 0.1})
        self.float_layout.add_widget(self.animal_image)
        
        self.animal2_image = Image(source='img/sheep.png', size_hint=(None, None), size=(1200, 360),
                                  pos_hint={'center_x': -1, 'center_y': 0.1})
        self.float_layout.add_widget(self.animal2_image)

        # Start Button
        self.start_button = Button(text="", font_size=24, size_hint=(None, None), 
                                   size=(600, 180),  
                                   pos_hint={'center_x': 0.5, 'center_y': -0.3},
                                   background_normal='img/start.png',
                                   background_down='img/start_pressed.png')
        self.start_button.bind(on_release=self.start_game)
        self.float_layout.add_widget(self.start_button)

        # Settings Button
        self.settings_button = Button(text="", font_size=24, size_hint=(None, None), 
                                      size=(600, 180),
                                      pos_hint={'center_x': 0.5, 'center_y': -0.5},
                                      background_normal='img/setting.png',
                                      background_down='img/setting_icon_pressed.png')
        self.settings_button.bind(on_release=self.open_settings)
        self.float_layout.add_widget(self.settings_button)

        # Add float layout to screen
        self.add_widget(self.float_layout)

        # Add rotation support for animal_image
        with self.animal_image.canvas.before:
            PushMatrix()
            self.rot = Rotate()
            self.rot.origin = (self.animal_image.center_x, self.animal_image.center_y)
        with self.animal_image.canvas.after:
            PopMatrix()

    def animate_widgets(self):
        # Animasi judul
        title_animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.8}, duration=1, t='out_bounce')
        title_animation.start(self.title_layout)
        
        # Animasi gambar animal1 (bergerak ke posisinya)
        animal1_animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.5}, duration=1, t='out_sine')
        animal1_animation.bind(on_complete=self.start_rotate_animation)  # Mulai animasi rotasi setelah ini selesai
        animal1_animation.start(self.animal_image)
        
        # Animasi sheep (bergerak dari kiri ke kanan secara berulang)
        self.start_sheep_animation()

        # Animasi tombol start
        start_button_animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.35}, duration=1, t='out_bounce')
        start_button_animation.start(self.start_button)

        # Animasi tombol settings
        settings_button_animation = Animation(pos_hint={'center_x': 0.5, 'center_y': 0.15}, duration=1.2, t='out_bounce')
        settings_button_animation.start(self.settings_button)

    def start_rotate_animation(self, *args):
        # Animasi rotasi setelah animasi pertama selesai
        rotate_animation = Animation(angle=5, duration=0.8) + \
                           Animation(angle=-5, duration=0.8)

        rotate_animation.repeat = True  # Mengulang animasi secara terus menerus
        rotate_animation.start(self.rot)

    def start_sheep_animation(self, *args):
        # Animasi sheep dari kiri ke kanan (looping)
        sheep_animation = Animation(pos_hint={'center_x': -2}, duration=6) + \
                          Animation(pos_hint={'center_x': 2}, duration=0)  # Kembali ke kiri langsung tanpa transisi
        sheep_animation.repeat = True  # Mengulang animasi terus menerus
        sheep_animation.start(self.animal2_image)

    def stop_animations(self):
        # Stop semua animasi aktif
        Animation.cancel_all(self.animal_image)
        Animation.cancel_all(self.animal2_image)
        Animation.cancel_all(self.rot)

    def on_leave(self):
        # Hentikan animasi saat meninggalkan screen untuk menghindari error
        self.stop_animations()

    def start_game(self, instance):
        self.manager.current = 'select_game'

    def open_settings(self, instance):
        self.manager.current = 'settings'
