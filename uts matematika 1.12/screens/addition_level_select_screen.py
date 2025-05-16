# addition_level_select_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class AdditionLevelSelectScreen(Screen):
    def __init__(self, **kwargs):
        super(AdditionLevelSelectScreen, self).__init__(**kwargs)

        self.completed_levels = [False] * 10

        # Add background image
        self.background = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Layout setup
        layout = BoxLayout(orientation='vertical')

        # Grid layout for level buttons
        self.grid = GridLayout(cols=5, rows=2, spacing=5, padding=[30, 50, 30, 50], size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5})
        self.level_buttons = []

        for i in range(10):
            button = Button(
                text=f"Level {i+1}",
                size_hint=(None, None),
                size=(320, 500),
                background_normal='img/lv_normal2.png',
                background_down='img/lv_normal2.png',
                background_disabled_normal='img/lv_disable.png',
                font_size='16sp',
                disabled=True if i != 0 else False
            )
            button.bind(on_release=self.start_level)
            self.level_buttons.append(button)
            self.grid.add_widget(button)

        layout.add_widget(self.grid)

        # Back button
        back_button = Button(
            text="",
            size_hint=(None, None),
            size=(140, 140),
            pos_hint={'x': 0.01, 'top': 0.95},
            background_normal='img/back1.png',
            background_down='img/back_icon_pressed.png',
        )
        back_button.bind(on_release=self.go_back)
        self.add_widget(back_button)  # Adding outside the main layout

        self.add_widget(layout)

    def start_level(self, instance):
        level_num = int(instance.text.split()[1])
        game_screen = self.manager.get_screen('addition_game')
        game_screen.start_level(level_num)
        self.manager.current = 'addition_game'

    def update_level_status(self, level_num):
        self.completed_levels[level_num - 1] = True
        if level_num < 10:
            self.level_buttons[level_num].disabled = False

        self.level_buttons[level_num - 1].background_normal = 'img/lv_completed.png'
        self.level_buttons[level_num - 1].background_down = 'img/lv_completed.png'

    def go_back(self, instance):
        self.manager.current = 'select_game'
