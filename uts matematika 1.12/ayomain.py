import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import SwapTransition
from kivy.animation import Animation

kivy.require('2.0.0')

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        loading_label = Label(text="Loading...", font_size=40)
        layout.add_widget(loading_label)
        self.add_widget(layout)

        self.sound = SoundLoader.load('sound/op.mp3')
        if self.sound:
            self.sound.loop = True
            self.sound.play()

        Clock.schedule_once(self.switch_to_menu, 4)

    def switch_to_menu(self, dt):
        if self.sound:
            self.sound.stop()
        self.manager.current = 'menu'

class MenuScreen(Screen):
    def on_enter(self):
        app = App.get_running_app()
        app.play_menu_music()

    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=[50, 50, 50, 50])

        background = Image(source='img/bg2.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(background)

        title_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.3))
        title = Image(source='img/text.png')
        title_layout.add_widget(title)
        layout.add_widget(title_layout)

        animal_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.3), padding=10)

        # animal_layout.add_widget(Image(source='img/monkey.png'))
        # animal_layout.add_widget(Image(source='img/tiger.png'))

        self.panda = Image(source='img/panda.png', size_hint=(None, None), size=(100, 100))
        animal_layout.add_widget(self.panda)
        self.animate_panda()

        # animal_layout.add_widget(Image(source='img/giraffe.png'))
        # animal_layout.add_widget(Image(source='img/sheep.png'))
        layout.add_widget(animal_layout)

        start_button = Button(text="", font_size=24, size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.3},
                              background_normal='img/start.png',
                              background_down='img/start-end.png')
        start_button.bind(on_release=self.start_game)
        layout.add_widget(start_button)

        settings_button = Button(text="", font_size=24, size_hint=(0.4, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.15},
                                 background_normal='img/setting.png',
                                 background_down='img/setting-end.png')
        settings_button.bind(on_release=self.open_settings)
        layout.add_widget(settings_button)

        self.add_widget(layout)

    def animate_panda(self):
        anim = Animation(x=Window.width - 100, duration=2) + Animation(x=0, duration=2)
        anim.repeat = True
        anim.start(self.panda)

    def start_game(self, instance):
        self.manager.current = 'select_game'

    def open_settings(self, instance):
        self.manager.current = 'settings'


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        bg_image = Image(source='img/bg2.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        float_layout = FloatLayout()

        with float_layout.canvas.before:
            Color(0, 0, 0, 0.5)
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 50, 20, 50], size_hint=(0.8, 0.8),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})

        self.music_volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(0.8, 0.2))
        self.sound_volume_slider = Slider(min=0, max=1, value=0.5, size_hint=(0.8, 0.2))

        layout.add_widget(Label(text="Volume Musik", font_size='20sp', color=(1, 1, 1, 1)))
        layout.add_widget(self.music_volume_slider)
        layout.add_widget(Label(text="Volume Suara", font_size='20sp', color=(1, 1, 1, 1)))
        layout.add_widget(self.sound_volume_slider)

        float_layout.add_widget(layout)

        back_button = Button(text="", size_hint=(None, None), size=(50, 50),
                             background_normal='img/back.png',
                             background_down='img/back_icon_pressed.png',
                             pos_hint={'x': 0, 'top': 0.95})
        back_button.bind(on_release=self.go_back)
        float_layout.add_widget(back_button)

        self.add_widget(float_layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def go_back(self, instance):
        self.manager.current = 'menu'


class SelectGameScreen(Screen):
    def __init__(self, **kwargs):
        super(SelectGameScreen, self).__init__(**kwargs)

        bg_image = Image(source='img/bg2.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=[20, 100, 20, 50])
        layout.size_hint = (None, None)
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.2}

        title_label = Label(text="Pilih Permainan", font_size='32sp', bold=True, color=(1, 0.5, 0, 1),
                            size_hint=(None, None), pos_hint={'center_x': 0.5})
        layout.add_widget(title_label)

        addition_button = Button(text="", size_hint=(None, None), size=(300, 100),
                                 background_normal='img/+++.png',
                                 background_down='img/add_icon_pressed.png', font_size='24sp', color=(0, 0, 0, 1),
                                 pos_hint={'center_x': 0.5})
        addition_button.bind(on_release=self.start_addition_game)
        layout.add_widget(addition_button)

        subtraction_button = Button(text="", size_hint=(None, None), size=(300, 100),
                                    background_normal='img/-.png',
                                    background_down='img/sub_icon_pressed.png', font_size='24sp', color=(0, 0, 0, 1),
                                    pos_hint={'center_x': 0.5})
        subtraction_button.bind(on_release=self.start_subtraction_game)
        layout.add_widget(subtraction_button)

        back_button = Button(text="", size_hint=(None, None), size=(50, 50),
                             background_normal='img/back.png',
                             background_down='img/back_icon_pressed.png', font_size='24sp', color=(0, 0, 0, 1),
                             pos_hint={'x': 0, 'top': 1})
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def start_addition_game(self, instance):
        game_screen = self.manager.get_screen('game')
        game_screen.set_game_mode('addition')
        self.manager.current = 'level_select'

    def start_subtraction_game(self, instance):
        game_screen = self.manager.get_screen('game')
        game_screen.set_game_mode('subtraction')
        self.manager.current = 'level_select'

    def go_back(self, instance):
        self.manager.current = 'menu'

class LevelSelectScreen(Screen):
    def __init__(self, **kwargs):
        super(LevelSelectScreen, self).__init__(**kwargs)
        
        bg_image = Image(source='img/bg2.png', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=[20, 50, 20, 50])
        
        back_button = Button(text="", size_hint=(None, None), size=(50, 50),
                             background_normal='img/back.png',
                             background_down='img/back_icon_pressed.png',
                             pos_hint={'x': 0, 'y': 0.9})
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        
        title_label = Label(text="Pilih Level", font_size='60sp', bold=True, color=(1, 0.5, 0, 1), size_hint=(1, 0.2))
        layout.add_widget(title_label)

        self.grid = GridLayout(cols=4, rows=2, spacing=10, padding=[50, 20, 50, 20], size_hint=(1, 0.6))
        self.level_buttons = []

        for i in range(8):
            button = Button(text=f"Level {i+1}", size_hint=(None, None), size=(200, 150))
            button.bind(on_release=self.start_level)
            button.disabled = True if i != 0 else False
            self.level_buttons.append(button)
            self.grid.add_widget(button)

        layout.add_widget(self.grid)

        self.add_widget(layout)

    def start_level(self, instance):
        level_num = int(instance.text.split()[1])
        game_screen = self.manager.get_screen('game')
        game_screen.start_level(level_num)
        self.manager.current = 'game'

    def update_level_status(self, level_num):
        self.completed_levels[level_num - 1] = True
        if level_num < 8:
            self.level_buttons[level_num].disabled = False
        
        self.level_buttons[level_num - 1].background_color = (1, 1, 0, 1)
        self.level_buttons[level_num - 1].text = f"Level {level_num}\n⭐⭐⭐"

    def go_back(self, instance):
        self.manager.current = 'select_game'


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10)
        self.question_label = Label(text="Soal", font_size=32)
        self.layout.add_widget(self.question_label)
        self.options_layout = BoxLayout(orientation='horizontal', spacing=10)
        self.layout.add_widget(self.options_layout)

        back_button = Button(text="Kembali", size_hint=(0.5, 0.2))
        back_button.bind(on_release=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def set_game_mode(self, mode):
        self.mode = mode

    def start_level(self, level):
        self.level = level
        self.display_question(level)

    def display_question(self, level):
        if self.mode == 'addition':
            questions = ["1 + 2 =", "3 + 4 =", "2 + 6 =", "5 + 3 =", "7 + 2 =", "8 + 1 =", "4 + 4 =", "6 + 3 =", "9 + 0 =", "8 + 9 ="]
            options = [[5, 3, 4], [7, 8, 5], [10, 11, 8], [9, 10, 8], [11, 12, 9], [7, 9, 8], [8, 5, 7], [9, 10, 7], [1, 4, 9], [13, 17, 19]]
            correct_answers = [3, 7, 8, 8, 9, 9, 8, 9, 9, 17]
        elif self.mode == 'subtraction':
            questions = ["3 - 1 =", "7 - 4 =", "8 - 6 =", "10 - 3 =", "12 - 9 =", "9 - 1 =", "8 - 4 =", "10 - 6 =", "9 - 0 =", "9 - 7 ="]
            options = [[2, 3, 4], [2, 3, 4], [1, 2, 3], [7, 8, 9], [3, 4, 5], [6, 7, 8], [4, 5, 6], [2, 4, 5], [0, 4, 9], [2, 5, 4]]
            correct_answers = [2, 3, 2, 7, 3, 8, 4, 4, 9, 2]

        self.correct_answer = correct_answers[level - 1]
        self.question_label.text = questions[level - 1]
        self.options_layout.clear_widgets()

        for option in options[level - 1]:
            button = Button(text=str(option), size_hint=(0.3, 0.2))
            button.bind(on_release=lambda x, ans=option: self.confirm_answer(ans))
            self.options_layout.add_widget(button)


    def confirm_answer(self, answer):
        if answer == self.correct_answer:
            self.show_popup(True)
        else:
            self.show_popup(False)


    def show_popup(self, correct):
        popup_layout = BoxLayout(orientation='vertical', spacing=10)
        if correct:
            popup_label = Label(text="Benar! Anda mendapatkan 3 bintang!", font_size=24)
            next_button = Button(text="Lanjut", size_hint=(0.3, 0.2))
            next_button.bind(on_release=self.next_level)
            popup_layout.add_widget(popup_label)
            popup_layout.add_widget(next_button)
        else:
            popup_label = Label(text="Salah! Coba lagi.", font_size=24)
            retry_button = Button(text="Ulang", size_hint=(0.3, 0.2))
            retry_button.bind(on_release=self.retry_level)
            popup_layout.add_widget(popup_label)
            popup_layout.add_widget(retry_button)
        
        self.popup = Popup(title="Hasil", content=popup_layout, size_hint=(0.6, 0.4))
        self.popup.open()

    def retry_level(self, instance):
        self.popup.dismiss()
        self.display_question(self.level)

    def next_level(self, instance):
        self.popup.dismiss()
        level_select_screen = self.manager.get_screen('level_select')
        level_select_screen.update_level_status(self.level)
        self.manager.current = 'level_select'

    def go_back(self, instance):
        self.manager.current = 'level_select'

class MathApp(App):
    def build(self):
        self.sound = None
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SelectGameScreen(name='select_game'))
        sm.add_widget(LevelSelectScreen(name='level_select'))
        sm.add_widget(GameScreen(name='game'))
        return sm

    def play_menu_music(self):

        if not self.sound:
            self.sound = SoundLoader.load('sound/backsound1.mp3')
        if self.sound:
            self.sound.loop = True
            self.sound.play()

    def stop_music(self):

        if self.sound:
            self.sound.stop()

if __name__ == '__main__':
    MathApp().run()