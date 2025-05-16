# addition_screen.py
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

class AdditionScreen(Screen):
    def __init__(self, **kwargs):
        super(AdditionScreen, self).__init__(**kwargs)
        self.mode = 'addition'
        self.current_question_index = 0  # Track the current question within the level
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

        # Timer label
        # Timer label
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
        self.current_question_index = 0
        self.start_timer()  # Applies the 90-second limit at the start of the level
        self.display_question(level, self.current_question_index)

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


    def display_question(self, level, question_index):
        self.start_timer()  # Reset timer for each new question

        # Define questions, options, and correct answers for addition mode
        addition_questions = [
                ["soal plus/soalp11.png", "soal plus/soalp12.png", "soal plus/soalp13.png", "soal plus/soalp14.png", "soal plus/soalp15.png"],  # Level 1
                ["soal plus/soalp21.png", "soal plus/soalp22.png", "soal plus/soalp23.png", "soal plus/soalp24.png", "soal plus/soalp25.png"],  # Level 2
                ["soal plus/soalp31.png", "soal plus/soalp32.png", "soal plus/soalp33.png", "soal plus/soalp34.png", "soal plus/soalp35.png"],  # Level 3
                ["soal plus/soalp41.png", "soal plus/soalp42.png", "soal plus/soalp43.png", "soal plus/soalp44.png", "soal plus/soalp45.png"],  # Level 4
                ["soal plus/soalp51.png", "soal plus/soalp52.png", "soal plus/soalp53.png", "soal plus/soalp54.png", "soal plus/soalp55.png"],  # Level 5
                
            ]
            
        addition_options = [
                [["jwb/4.png", "jwb/5.png", "jwb/6.png"], ["jwb/3.png", "jwb/5.png", "jwb/4.png"], ["jwb/5.png", "jwb/6.png", "jwb/7.png"], ["jwb/2.png", "jwb/3.png", "jwb/4.png"], ["jwb/7.png", "jwb/8.png", "jwb/9.png"]],
                [["jwb/11.png", "jwb/12.png", "jwb/13.png"], ["jwb/13.png", "jwb/14.png", "jwb/12.png"], ["jwb/12.png", "jwb/13.png", "jwb/14.png"], ["jwb/12.png", "jwb/13.png", "jwb/14.png"], ["jwb/14.png", "jwb/15.png", "jwb/16.png"]],
                [["jwb/21.png", "jwb/22.png", "jwb/23.png"], ["jwb/23.png", "jwb/24.png", "jwb/25.png"], ["jwb/23.png", "jwb/24.png", "jwb/25.png"], ["jwb/25.png", "jwb/26.png", "jwb/27.png"], ["jwb/23.png", "jwb/24.png", "jwb/25.png"]],
                [["jwb/26.png", "jwb/27.png", "jwb/30.png"], ["jwb/28.png", "jwb/29.png", "jwb/30.png"], ["jwb/30.png", "jwb/31.png", "jwb/35.png"], ["jwb/27.png", "jwb/28.png", "jwb/29.png"], ["jwb/30.png", "jwb/31.png", "jwb/32.png"]],
                [["jwb/40.png", "jwb/41.png", "jwb/42.png"], ["jwb/59.png", "jwb/60.png", "jwb/61.png"], ["jwb/66.png", "jwb/67.png", "jwb/28.png"], ["jwb/83.png", "jwb/84.png", "jwb/85.png"], ["jwb/90.png", "jwb/100.png", "jwb/110.png"]],
            ]
        addition_correct_answers = [
                ["jwb/5.png", "jwb/5.png", "jwb/6.png", "jwb/4.png", "jwb/7.png"],  # Level 1
                ["jwb/13.png", "jwb/14.png", "jwb/14.png", "jwb/14.png", "jwb/15.png"],  # Level 2
                ["jwb/23.png", "jwb/23.png", "jwb/25.png", "jwb/25.png", "jwb/25.png"],  # Level 3
                ["jwb/30.png", "jwb/29.png", "jwb/30.png", "jwb/29.png", "jwb/32.png"],  # Level 4
                ["jwb/42.png", "jwb/60.png", "jwb/68.png", "jwb/85.png", "jwb/100.png"],  # Level 5
            ]

        self.question_image.source = addition_questions[level - 1][question_index]
        self.correct_answer = addition_correct_answers[level - 1][question_index]
        
        # Clear existing options and display new ones
        self.options_layout.clear_widgets()
        for option in addition_options[level - 1][question_index]:
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
        
        # Display different popups based on correctness
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
        if self.current_question_index < 4:
            self.current_question_index += 1
            self.display_question(self.level, self.current_question_index)
        else:
            self.manager.current = 'addition_level_select'

    def retry_level_and_close(self, popup_view):
        popup_view.dismiss()
        self.display_question(self.level, self.current_question_index)

    def go_back(self, instance):
        self.manager.current = 'addition_level_select'
