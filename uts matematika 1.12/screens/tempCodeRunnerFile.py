from kivy.app import App
from kivy.uix.video import Video

class TestVideoApp(App):
    def build(self):
        # Membuat dan mendefinisikan objek video dengan path yang benar
        self.video = Video(source='D:/KULIAH/2024/Semester 5/Pemograman Python/uts matematika 1.9/video/loading-white.mp4', state='play', options={'eos': 'loop'})
        return self.video

# Jalankan aplikasi
if __name__ == '__main__':
    TestVideoApp().run()
