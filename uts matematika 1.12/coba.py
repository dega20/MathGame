from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens.loading_screen import LoadingScreen
from screens.menu_screen import MenuScreen
from screens.settings_screen import SettingsScreen
from screens.select_game_screen import SelectGameScreen
from screens.level_select_screen import LevelSelectScreen
from screens.game_screen import GameScreen
from screens.pilih import PilihScreen
from audio import play_menu_music
from kivy.uix.video import Video
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Layar loading yang memutar video
class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        # Membuat dan mendefinisikan objek video dengan path yang benar
        self.video = Video(source='D:/KULIAH/2024/Semester 5/Pemograman Python/uts matematika 1.9/video/loading-white.mp4', state='play', options={'eos': 'loop'})
        self.add_widget(self.video)

    def on_enter(self):
        # Mulai video saat layar loading dibuka
        self.video.state = 'play'
        # Menjalankan fungsi switch_to_menu setelah 10 detik
        Clock.schedule_once(self.switch_to_menu, 10)

    def switch_to_menu(self, dt):
        # Berpindah ke layar menu setelah loading selesai
        self.manager.current = 'menu'

    def on_leave(self):
        # Hentikan video saat keluar dari layar
        self.video.state = 'stop'


# Aplikasi utama dengan ScreenManager
class TestVideoApp(App):
    def build(self):
        self.sound = None
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name='loading'))  # Layar loading dengan video
        sm.add_widget(MenuScreen(name='menu'))  # Layar menu
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SelectGameScreen(name='select_game'))
        sm.add_widget(LevelSelectScreen(name='level_select'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(PilihScreen(name='pilih'))
        return sm
    def play_menu_music(self):
        play_menu_music(self)

# Jalankan aplikasi
if __name__ == '__main__':
    TestVideoApp().run()
