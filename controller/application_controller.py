from termcolor import colored
from .game_controller import GameController
from .arithmetic_controller import AdditionController, SubtractionController, MultiplicationController, DivisionController

class ApplicationController:
    @classmethod
    def start_game(cls):
        print(colored("暗算トレーニングアプリケーション 起動...", "cyan"))
        selected_game = GameController.choose_problem()
        if selected_game == "a":
            AdditionController.start()
        elif selected_game == "s":
            SubtractionController.start()
        elif selected_game == "m":
            MultiplicationController.start()
        elif selected_game == "d":
            DivisionController.start()
