from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

class LevelSelectScreen(Screen):
    def __init__(self, **kwargs):
        super(LevelSelectScreen, self).__init__(**kwargs)

        self.completed_levels = [False] * 10

        # Add background image
        self.background = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(self.background)

        # Create a layout on top of the background
        layout = BoxLayout(orientation='vertical')

        # Create grid layout for level buttons
        self.grid = GridLayout(cols=5, rows=2, spacing=10, padding=[50, 70, 50, 70], size_hint=(0.9, 0.6), pos_hint={'center_x': 0.5})
        self.level_buttons = []

        for i in range(10):
            button = Button(
                text=f"Level {i+1}",
                size_hint=(0.8, 0.8),
                background_normal='img/lv2.jpg',  # Always use the image as background
                background_down='img/lv2.jpg',
                background_disabled_normal='img/lv_disable.png',  # Use the same image when disabled
                font_size='16sp',
                halign='center',
                valign='middle',
                disabled=True if i != 0 else False  # Only enable the first level by default
            )
            button.bind(on_release=self.start_level)
            self.level_buttons.append(button)
            self.grid.add_widget(button)

        layout.add_widget(self.grid)

        # Create a back button and place it at the top left corner
        back_button = Button(
            text="", 
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'x': 0.05, 'top': 1},  # Position at top left
            background_normal='img/back.png',
            background_down='img/sub_icon_pressed.png',
             
        )
        back_button.bind(on_release=self.go_back)
        self.add_widget(back_button)  # Add back button to the screen, outside the main layout

        self.add_widget(layout)


    def start_level(self, instance):
        level_num = int(instance.text.split()[1])
        game_screen = self.manager.get_screen('game')
        game_screen.start_level(level_num)
        self.manager.current = 'game'

    def update_level_status(self, level_num):
        self.completed_levels[level_num - 1] = True
        if level_num < 10:
            self.level_buttons[level_num].disabled = False

        # Change appearance of completed levels
        self.level_buttons[level_num - 1].background_normal = 'img/lv_completed.png'
        self.level_buttons[level_num - 1].background_down = 'img/lv_completed.png'

    def go_back(self, instance):
        self.manager.current = 'select_game'
