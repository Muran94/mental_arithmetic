from .game_controller import GameController
from arithmetic.arithmetic import Addition, Subtraction, Multiplication, Division

class ApplicationController:
    @classmethod
    def start_game(cls):
        print("暗算トレーニングアプリケーション 起動...")
        selected_game = GameController.choose_problem()
        if selected_game == "a":
            Addition.start()
        elif selected_game == "s":
            Subtraction.start()
        elif selected_game == "m":
            Multiplication.start()
        elif selected_game == "d":
            Division.start()
