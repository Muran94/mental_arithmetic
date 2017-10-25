from config.game_setting import GameSetting

import re

from random import randint

class Addition:
    def __init__(self):
        self.correct_answer_count = 0

    def start(self):
        for i in range(1, 11):
            problem = self.create_problem()
            self.get_user_answer(problem)
        print("結果 : {0}/10".format(self.correct_answer_count))

    def create_problem(self):
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        self.correct_answer = num1 + num2
        return "{0:>3d} + {1:>3d} = ".format(num1, num2)

    def get_user_answer(self, problem):
        while True:
            user_answer = input(problem)

            if re.match(r"^[0-9]+$", user_answer):
                if int(user_answer) == self.correct_answer:
                    self.correct_answer_count += 1
                    print("正解")
                    break
                else:
                    print("不正解")
                    break
            else:
                print("入力された値に誤りがあります")

class MentalArithmeticApplication:
    def __init__(self, selected_game):
        self.selected_game = selected_game
        self.startgame(self.selected_game)

    def startgame(self, selected_game):
        if selected_game == "a":
            addition = Addition()
            addition.start()
        elif selected_game == "s":
            pass
        elif selected_game == "m":
            pass
        elif selected_game == "d":
            pass



game_setting = GameSetting()
selected_game = game_setting.select_game()

mental_arithmetic_application = MentalArithmeticApplication(selected_game)
