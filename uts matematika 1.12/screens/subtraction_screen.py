from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.modalview import ModalView

class SubtractionScreen(Screen):
    def __init__(self, **kwargs):
        super(SubtractionScreen, self).__init__(**kwargs)
        self.mode = 'subtraction'
        self.current_question_index = 0
        self.time_limit = 30  # 1 minute and 30 seconds per level
        self.time_left = self.time_limit  # Initialize time left
        self.timer_event = None  # Timer event for countdown
        self.setup_layout()

    def setup_layout(self):
        # Background image
        bg_image = Image(source='img/bg3.jpg', allow_stretch=True, keep_ratio=False)
        self.add_widget(bg_image)

        # FloatLayout for transparent layer and game content
        float_layout = FloatLayout()

        # Add transparent layer
        with float_layout.canvas.before:
            Color(0, 0, 0, 0.5)
            self.rect = Rectangle(size=Window.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

        # Layout for game content
        layout = BoxLayout(orientation='vertical', spacing=10, padding=[20, 50, 20, 50], size_hint=(0.8, 0.8), pos_hint={'center_x': 0.5, 'center_y': 0.75})

        # Question label
        self.question_image = Image(source='img/default_question.png', size_hint=(1, 0.6))
        layout.add_widget(self.question_image)

        self.timer_label = Label(text="Time: 30", font_size='24sp',font_name='Roboto-Bold',  # Pastikan font ini tersedia atau gunakan font tebal lainnya
    color=(0, 0, 0, 1), size_hint=(None, None), size=(200, 50),
                                 pos_hint={'right': 1, 'top': 1})
        
        float_layout.add_widget(self.timer_label)  # Add 

        # Options layout for answer buttons
        self.options_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint=(None, None), pos_hint={'center_x': 0.564})
        self.options_layout.width = 400
        self.options_layout.height = 100
        layout.add_widget(self.options_layout)

        # Back button
        back_button = Button(text="", size_hint=(None, None), size=(140, 140),
                             background_normal='img/back1.png',
                             background_down='img/back_icon_pressed.png',
                             pos_hint={'x': 0.01, 'top': 0.95})
        back_button.bind(on_release=self.go_back)
        float_layout.add_widget(back_button)

        float_layout.add_widget(layout)
        self.add_widget(float_layout)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

    def start_level(self, level):
        self.level = level
        self.current_question_index = 0  # Reset question index for each new level
        self.start_timer()
        self.display_question()

    def start_timer(self):
        self.time_left = self.time_limit
        self.update_timer_label()
        if self.timer_event:
            self.timer_event.cancel()
        self.timer_event = Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        self.time_left -= 1
        self.update_timer_label()
        if self.time_left <= 0:
            self.timer_event.cancel()
            self.show_popup(correct=False)

    def update_timer_label(self):
        minutes = self.time_left // 60
        seconds = self.time_left % 60
        self.timer_label.text = f"Time: {minutes}:{seconds:02d}"

    def display_question(self):
        # Data setup
        self.start_timer() 
        subtraction_questions = [
                ["soal minus/soalm11.png", "soal minus/soalm12.png", "soal minus/soalm13.png", "soal minus/soalm14.png", "soal minus/soalm15.png"],  # Level 1
                ["soal minus/soalm21.png", "soal minus/soalm22.png", "soal minus/soalm23.png", "soal minus/soalm24.png", "soal minus/soalm25.png"],  # Level 2
                ["soal minus/soalm31.png", "soal minus/soalm32.png", "soal minus/soalm33.png", "soal minus/soalm34.png", "soal minus/soalm35.png"],  # Level 3
                ["soal minus/soalm41.png", "soal minus/soalm42.png", "soal minus/soalm43.png", "soal minus/soalm44.png", "soal minus/soalm45.png"],  # Level 4
                ["soal minus/soalm51.png", "soal minus/soalm52.png", "soal minus/soalm53.png", "soal minus/soalm54.png", "soal minus/soalm55.png"],  # Level 5
            ]
        subtraction_options = [
                [["jwb/2.png", "jwb/3.png", "jwb/4.png"], ["jwb/2.png", "jwb/3.png", "jwb/4.png"], ["jwb/3.png", "jwb/2.png", "jwb/1.png"], ["jwb/1.png", "jwb/3.png", "jwb/2.png"], ["jwb/1.png", "jwb/2.png", "jwb/4.png"]],
                [["jwb/3.png", "jwb/4.png", "jwb/1.png"], ["jwb/3.png", "jwb/5.png", "jwb/4.png"], ["jwb/5.png", "jwb/3.png", "jwb/4.png"], ["jwb/2.png", "jwb/1.png", "jwb/0.png"], ["jwb/3.png", "jwb/4.png", "jwb/2.png"]],
                [["jwb/4.png", "jwb/3.png", "jwb/2.png"], ["jwb/4.png", "jwb/3.png", "jwb/2.png"], ["jwb/3.png", "jwb/2.png", "jwb/1.png"], ["jwb/4.png", "jwb/3.png", "jwb/2.png"], ["jwb/1.png", "jwb/2.png", "jwb/0.png"]],
                [["jwb/4.png", "jwb/3.png", "jwb/2.png"], ["jwb/6.png", "jwb/7.png", "jwb/5.png"], ["jwb/7.png", "jwb/8.png", "jwb/6.png"], ["jwb/4.png", "jwb/5.png", "jwb/6.png"], ["jwb/4.png", "jwb/5.png", "jwb/6.png"]],
                [["jwb/8.png", "jwb/10.png", "jwb/9.png"], ["jwb/13.png", "jwb/14.png", "jwb/15.png"], ["jwb/24.png", "jwb/23.png", "jwb/22.png"], ["jwb/26.png", "jwb/25.png", "jwb/24.png"], ["jwb/20.png", "jwb/19.png", "jwb/18.png"]],
            ]
        subtraction_correct_answers = [
                ["jwb/2.png", "jwb/2.png", "jwb/2.png", "jwb/1.png", "jwb/1.png"],  # Level 1
                ["jwb/3.png", "jwb/3.png", "jwb/3.png", "jwb/1.png", "jwb/1.png"],  # Level 2
                ["jwb/3.png", "jwb/3.png", "jwb/3.png", "jwb/2.png", "jwb/2.png"],  # Level 3
                ["jwb/4.png", "jwb/7.png", "jwb/8.png", "jwb/5.png", "jwb/5.png"],  # Level 4
                ["jwb/10.png", "jwb/15.png", "jwb/23.png", "jwb/25.png", "jwb/20.png"],  # Level 5
            ]

        # Set question image and correct answer based on level and current question index
        self.correct_answer = subtraction_correct_answers[self.level - 1][self.current_question_index]
        self.question_image.source = subtraction_questions[self.level - 1][self.current_question_index]

        # Clear existing option buttons
        self.options_layout.clear_widgets()

        # Populate options with new buttons based on the question's options
        for option in subtraction_options[self.level - 1][self.current_question_index]:
            button = Button(size_hint=(None, None), size=(100, 100), background_normal=option, background_down=option)
            button.bind(on_release=lambda x, ans=option: self.confirm_answer(ans))
            self.options_layout.add_widget(button)

    def confirm_answer(self, answer):
        if self.timer_event:
            self.timer_event.cancel()  # Stop timer when answer is confirmed
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
            next_button.bind(on_release=lambda x: self.next_question_or_level(popup_view))
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

    def next_question_or_level(self, popup_view):
        popup_view.dismiss()
        # Check if there are more questions in the level
        if self.current_question_index < 4:  # Assuming each level has 5 questions
            self.current_question_index += 1
            self.display_question()
        else:
            # Move back to level selection when level is complete
            level_select_screen = self.manager.get_screen('subtraction_level_select')
            level_select_screen.update_level_status(self.level)
            self.manager.current = 'subtraction_level_select'

    def retry_level_and_close(self, popup_view):
        popup_view.dismiss()
        self.display_question()  # Redisplay the current question for retry

    def go_back(self, instance):
        self.manager.current = 'subtraction_level_select'
