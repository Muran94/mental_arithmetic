from config.game_setting import GameSetting
from arithmetic.arithmetic import Addition, Subtraction
import re

class MentalArithmeticApplication:
    def __init__(self, selected_game):
        self.selected_game = selected_game
        self.startgame(self.selected_game)

    def startgame(self, selected_game):
        if selected_game == "a":
            addition = Addition()
            addition.start()
        elif selected_game == "s":
            subtraction = Subtraction()
            subtraction.start() # ここらへんってクラスメソッドとして定義するだけで十分じゃないの？
        elif selected_game == "m":
            pass
        elif selected_game == "d":
            pass



game_setting = GameSetting()
selected_game = game_setting.select_game()

mental_arithmetic_application = MentalArithmeticApplication(selected_game)
