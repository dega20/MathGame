from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.modalview import ModalView

class GameScreen(Screen):
    def __init__(self, **kwargs):  # Perbaiki init dengan dua underscore
        super(GameScreen, self).__init__(**kwargs)

        # Add background image
        bg_image = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        # Create FloatLayout for transparent layer and game content
        float_layout = FloatLayout()

        # Add transparent layer
        with float_layout.canvas.before:
            Color(0, 0, 0, 0.5)  # 50% transparency
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        # Create layout for the game content
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 50, 20, 50], size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.75})

        # Question label
        self.question_image = Image(source='img/default_question.png', size_hint=(1, 0.6))
        layout.add_widget(self.question_image)

        # Options layout for answer buttons
        self.options_layout = BoxLayout(orientation='horizontal', spacing=20, padding=[0, 0, 0, 0], size_hint=(None, None), pos_hint={'center_x': 0.5})
        self.options_layout.width = 400  # Set a fixed width that adapts to content
        self.options_layout.height = 100  # Set height explicitly
        layout.add_widget(self.options_layout)

        # Back button
        back_button = Button(text="", size_hint=(None, None), size=(140, 140),
                             background_normal='img/back1.png',
                             background_down='img/back_icon_pressed.png',
                             pos_hint={'x': 0.01, 'top': 0.95})
        back_button.bind(on_release=self.go_back)
        float_layout.add_widget(back_button)

        # Add the game content layout to the float layout
        float_layout.add_widget(layout)

        # Finally, add the float layout to the GameScreen
        self.add_widget(float_layout)

    # Method to adjust background size and position when window resizes
    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def set_game_mode(self, mode):
        self.mode = mode

    def start_level(self, level):
        self.level = level
        self.display_question(level)

    def display_question(self, level):
        if self.mode == 'addition':
            questions = ["soal/soal 1.png", "soal/soal 2.png", "soal/soal 3.png", "soal/soal 4.png", "soal/soal 5.png", "soal/soal 6.png", "soal/soal 7.png", "soal/soal 8.png", "soal/soal 9.png", "soal/soal 10.png",]
            options = [["jwb/5.png", "jwb/3.png", "jwb/4.png"],
                       ["jwb/7.png", "jwb/8.png", "jwb/5.png"],
                       ["jwb/10.png", "jwb/11.png", "jwb/8.png"],
                       ["jwb/9.png", "jwb/10.png", "jwb/8.png"],
                       ["jwb/11.png", "jwb/12.png", "jwb/9.png"],
                       ["jwb/7.png", "jwb/9.png", "jwb/8.png"],
                       ["jwb/8.png", "jwb/5.png", "jwb/7.png"],
                       ["jwb/9.png", "jwb/10.png", "jwb/7.png"],
                       ["jwb/1.png", "jwb/4.png", "jwb/9.png"],
                       ["jwb/13.png", "jwb/17.png", "jwb/19.png"]]
            correct_answers = ["jwb/3.png", "jwb/7.png", "jwb/8.png", "jwb/8.png", "jwb/9.png", "jwb/9.png", "jwb/8.png", "jwb/9.png", "jwb/9.png", "jwb/17.png"]
        elif self.mode == 'subtraction':
            questions = ["soal k/soal 11.png", "soal k/soal 12.png", "soal k/soal 13.png", "soal k/soal 14.png", "soal k/soal 15.png", "soal k/soal 16.png", "soal k/soal 17.png", "soal k/soal 18.png", "soal k/soal 19.png", "soal k/soal 20.png",]
            options = [["jwb/2.png", "jwb/3.png", "jwb/4.png"],
                       ["jwb/2.png", "jwb/3.png", "jwb/4.png"],
                       ["jwb/1.png", "jwb/2.png", "jwb/3.png"],
                       ["jwb/7.png", "jwb/8.png", "jwb/9.png"],
                       ["jwb/3.png", "jwb/4.png", "jwb/5.png"],
                       ["jwb/6.png", "jwb/7.png", "jwb/8.png"],
                       ["jwb/4.png", "jwb/5.png", "jwb/6.png"],
                       ["jwb/2.png", "jwb/4.png", "jwb/5.png"],
                       ["jwb/2.png", "jwb/4.png", "jwb/9.png"],
                       ["jwb/2.png", "jwb/5.png", "jwb/4.png"]]
            correct_answers = ["jwb/2.png", "jwb/3.png", "jwb/2.png", "jwb/7.png", "jwb/3.png", "jwb/8.png", "jwb/4.png", "jwb/4.png", "jwb/9.png", "jwb/2.png"]

        self.correct_answer = correct_answers[level - 1]
        self.question_image.source = questions[level - 1]
        self.options_layout.clear_widgets()

        # Adjusted size for the buttons to make the images smaller
        for index, option in enumerate(options[level - 1]):
            button = Button(size_hint=(None, None), size=(100, 100), background_normal=option, background_down=option)
            button.bind(on_release=lambda x, ans=option: self.confirm_answer(ans))  # Pass image path as ans
            self.options_layout.add_widget(button)

    def confirm_answer(self, answer):
        if answer == self.correct_answer:
            self.show_popup(True)
        else:
            self.show_popup(False)

    def show_popup(self, correct):
        popup_view = ModalView(size_hint=(None, None), size=(600, 400), background_color=(0, 0, 0, 0), auto_dismiss=False)

        float_layout = FloatLayout()

        if correct:
            png_image = Image(source='img/popup-benar.png', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(900, 600), pos_hint={'center_x': 0.5, 'y': 0})
            next_button = Button(size_hint=(None, None), size=(350, 100), pos_hint={'center_x': 0.5, 'y': 0.38}, background_color=(0, 0, 0, 0), text="", color=(1, 1, 1, 0))
            next_button.bind(on_release=lambda x: self.next_level_and_close(popup_view))
            float_layout.add_widget(png_image)
            float_layout.add_widget(next_button)
        else:
            png_image = Image(source='img/popup-salah.png', allow_stretch=True, keep_ratio=False, size_hint=(None, None), size=(900, 600), pos_hint={'center_x': 0.5, 'y': 0})
            retry_button = Button(size_hint=(None, None), size=(350, 100), pos_hint={'center_x': 0.5, 'y': 0.38}, background_color=(0, 0, 0, 0), text="", color=(1, 1, 1, 0))
            retry_button.bind(on_release=lambda x: self.retry_level_and_close(popup_view))
            float_layout.add_widget(png_image)
            float_layout.add_widget(retry_button)

        popup_view.add_widget(float_layout)
        popup_view.open()

    def next_level_and_close(self, popup_view):
        popup_view.dismiss()
        level_select_screen = self.manager.get_screen('level_select')
        level_select_screen.update_level_status(self.level)
        self.manager.current = 'level_select'

    def retry_level_and_close(self, popup_view):
        popup_view.dismiss()
        self.display_question(self.level)

    def go_back(self, instance):
        self.manager.current = 'level_select'
