import re
from termcolor import colored

class GameController:
    @classmethod
    def choose_problem(cls):
        print("""
        足し算 : a
        引き算 : s
        掛け算 : m
        割り算 : d
        """)
        return cls.get_user_input()

    @classmethod
    def get_user_input(cls):
        while True:
            selected_game = input(colored("どの問題を解きますか？ => ", "cyan"))
            if re.match(r"^a|s|m|d$", selected_game):
                return selected_game
            else:
                print(colored("入力値に誤りがあります。もう一度入力してください。", "red"))
