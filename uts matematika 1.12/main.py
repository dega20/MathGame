from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.loading_screen import LoadingScreen
from screens.menu_screen import MenuScreen
from screens.settings_screen import SettingsScreen
from screens.select_game_screen import SelectGameScreen
from screens.level_select_screen import LevelSelectScreen
from screens.game_screen import GameScreen

from screens.addition_level_select_screen import AdditionLevelSelectScreen
from screens.subtraction_level_select_screen import SubtractionLevelSelectScreen
from screens.addition_screen import AdditionScreen
from screens.subtraction_screen import SubtractionScreen
from screens.pilih import PilihScreen
from audio import play_menu_music

class MathApp(App):
    def build(self):
        self.sound = None
        sm = ScreenManager()
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(SelectGameScreen(name='select_game'))
        sm.add_widget(LevelSelectScreen(name='level_select'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(AdditionLevelSelectScreen(name='addition_level_select'))
        sm.add_widget(SubtractionLevelSelectScreen(name='subtraction_level_select'))
        sm.add_widget(AdditionScreen(name='addition_game'))
        sm.add_widget(SubtractionScreen(name='subtraction_game'))
        sm.add_widget(PilihScreen(name='pilih'))

        self.play_menu_music()
        return sm

    def play_menu_music(self):
        self.sound = play_menu_music()

    def set_music_volume(self, volume):
        if self.sound:
            self.sound.volume = volume

if __name__ == '__main__':
    MathApp().run()
