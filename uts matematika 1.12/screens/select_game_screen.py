from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.animation import Animation

class SelectGameScreen(Screen):
    def on_enter(self):
        self.animate_widgets_in()

    def on_leave(self):
        self.animate_widgets_out()

    def __init__(self, **kwargs):
        super(SelectGameScreen, self).__init__(**kwargs)

        # Background image
        bg_image = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        # Main layout
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=[20, 100, 20, 50])
        self.layout.size_hint = (None, None)
        self.layout.pos_hint = {'center_x': 0.5, 'center_y': 0.3}
        self.add_widget(self.layout)

        # Title image
        self.title_image = Image(source='img/pilih_mode.png', size_hint=(None, None), size=(300, 100),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.1}, opacity=0)
        self.layout.add_widget(self.title_image)

        # Layout for buttons to make them side by side
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), size=(640, 100),
                                  pos_hint={'center_x': 0.5})
        
        # Addition button
        self.addition_button = Button(text="", size_hint=(None, None), size=(300, 100),
                                      background_normal='img/+++.png',
                                      background_down='img/jmlh.png', font_size='24sp', color=(0, 0, 0, 1),
                                      opacity=0)
        self.addition_button.bind(on_press=self.on_button_press)
        self.addition_button.bind(on_release=self.start_addition_level_select)

        # Subtraction button
        self.subtraction_button = Button(text="", size_hint=(None, None), size=(300, 100),
                                         background_normal='img/-.png',
                                         background_down='img/kurang.png', font_size='24sp', color=(0, 0, 0, 1),
                                         opacity=0)
        self.subtraction_button.bind(on_press=self.on_button_press)
        self.subtraction_button.bind(on_release=self.start_subtraction_level_select)

        # Add buttons to the layout
        button_layout.add_widget(self.addition_button)
        button_layout.add_widget(self.subtraction_button)
        self.layout.add_widget(button_layout)

        # Back button
        self.back_button = Button(text="", size_hint=(None, None), size=(140, 140),
                                  background_normal='img/back1.png',
                                  background_down='img/back_icon_pressed.png',
                                  pos_hint={'center_x': 0.01, 'top': 0.95})
        self.back_button.bind(on_release=self.go_back)
        self.add_widget(self.back_button)

        # Adding animal images
        self.animal1 = Image(source='img/tiger.png', size_hint=(None, None), size=(150, 150),
                             pos_hint={'center_x': 0.3, 'center_y': 0.15})
        self.add_widget(self.animal1)

        # Monkey image that will animate swinging
        self.monkey = Image(source='img/monkey.png', size_hint=(None, None), size=(150, 150),
                            pos_hint={'right': 1, 'top': 1})
        self.add_widget(self.monkey)

        # Start monkey animation
        self.start_monkey_swing_animation(self.monkey)

    def on_button_press(self, instance):
        anim = Animation(size=(290, 90), duration=0.1) + Animation(size=(300, 100), duration=0.1)
        anim.start(instance)

    def animate_widgets_in(self):
        title_anim = Animation(opacity=1, pos_hint={'center_y': 0.6}, duration=0.7, t='out_back') + Animation(size=(2400, 800), duration=0.2)
        self.title_image.size = (0, 0)
        title_anim.start(self.title_image)

        addition_button_anim = Animation(opacity=1, pos_hint={'center_x': 0.5}, duration=0.8, t='out_bounce')
        self.addition_button.opacity = 0
        self.addition_button.pos_hint = {'center_x': -0.5}
        addition_button_anim.start(self.addition_button)

        subtraction_button_anim = Animation(opacity=1, pos_hint={'center_x': 0.5}, duration=0.8, t='out_bounce')
        self.subtraction_button.opacity = 0
        self.subtraction_button.pos_hint = {'center_x': 1.5}
        subtraction_button_anim.start(self.subtraction_button)

        back_button_anim = Animation(pos_hint={'center_x': 0.05}, opacity=1, duration=0.8, t='out_quad')
        self.back_button.opacity = 0
        self.back_button.pos_hint = {'center_x': -0.2, 'top': 0.95}
        back_button_anim.start(self.back_button)

    def animate_widgets_out(self):
        title_anim = Animation(opacity=0, duration=0.5, t='in_quad') + Animation(size=(0, 0), duration=0.2)
        title_anim.start(self.title_image)

        addition_button_anim = Animation(opacity=0, pos_hint={'center_x': -0.5}, duration=0.5, t='in_quad')
        addition_button_anim.start(self.addition_button)

        subtraction_button_anim = Animation(opacity=0, pos_hint={'center_x': 1.5}, duration=0.5, t='in_quad')
        subtraction_button_anim.start(self.subtraction_button)

        back_button_anim = Animation(opacity=0, pos_hint={'center_x': -0.2}, duration=0.5, t='in_quad')
        back_button_anim.start(self.back_button)

    def start_monkey_swing_animation(self, monkey):
        def swing_left(*args):
            anim = Animation(pos_hint={'right': 0.98}, duration=1.5, t='in_out_quad')
            anim.bind(on_complete=swing_right)
            anim.start(monkey)

        def swing_right(*args):
            anim = Animation(pos_hint={'right': 1.02}, duration=1.5, t='in_out_quad')
            anim.bind(on_complete=swing_left)
            anim.start(monkey)

        swing_right()

    def start_addition_level_select(self, instance):
        self.manager.current = 'addition_level_select'

    def start_subtraction_level_select(self, instance):
        self.manager.current = 'subtraction_level_select'

    def go_back(self, instance):
        self.manager.current = 'menu'
