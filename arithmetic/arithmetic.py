""" メモ
四則演算のそれぞれのクラスのinitとstartとget_user_answerは共通化できる。要リファクタリング。
"""

from random import randint
import re

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

class Subtraction:
    def __init__(self):
        self.correct_answer_count = 0

    def start(self):
        for i in range(1, 11):
            problem = self.create_problem()
            self.get_user_answer(problem)
        print("結果 : {0}/10".format(self.correct_answer_count))

    def create_problem(self):
        num1 = randint(1, 999)
        num2 = randint(num1, 1000)
        self.correct_answer = num2 - num1
        return "{0:>3d} - {1:>3d} = ".format(num2, num1)

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

class Multiplication:
    def __init__(self):
        self.correct_answer_count = 0

    def start(self):
        for i in range(1, 11):
            problem = self.create_problem()
            self.get_user_answer(problem)
        print("結果 : {0}/10".format(self.correct_answer_count))

    def create_problem(self):
        num1 = randint(1, 99)
        num2 = randint(1, 99)
        self.correct_answer = num2 * num1
        return "{0:>3d} × {1:>3d} = ".format(num1, num2)

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

class Division:
    def __init__(self):
        self.correct_answer_count = 0

    def start(self):
        for i in range(1, 11):
            problem = self.create_problem()
            self.get_user_answer(problem)
        print("結果 : {0}/10".format(self.correct_answer_count))

    def create_problem(self):
        while True:
            num1 = randint(1, 100)
            num2 = randint(num1, 1000)
            if num2 % num1 == 0:
                break
        self.correct_answer = num2 / num1
        return "{0:>3d} ÷ {1:>3d} = ".format(num2, num1)

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
