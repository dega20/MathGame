from kivy.uix.screenmanager import Screen
from kivy.uix.video import Video
from kivy.clock import Clock

class LoadingScreen(Screen):
    def __init__(self, **kwargs):
        super(LoadingScreen, self).__init__(**kwargs)
        # Membuat dan mendefinisikan objek video dengan path yang benar
        self.video = Video(source='video/loading-white720p.mp4', state='play', options={'eos': 'loop'})
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
