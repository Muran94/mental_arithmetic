import re

class GameSetting:
    def select_game(self):
        print("""
        足し算 : a
        引き算 : s
        掛け算 : m
        割り算 : d
        """)
        return self.get_user_input()

    def get_user_input(self):
        while True:
            selected_game = input("よお、どれやってく？ => ")
            if re.match(r"^a|s|m|d$", selected_game):
                return selected_game
            else:
                print("もう一回入力せえやボケ")
