from kivy.core.audio import SoundLoader

def play_menu_music():
    sound = SoundLoader.load('.mp3')
    if sound:
        sound.loop = True
        sound.play()
    return sound
