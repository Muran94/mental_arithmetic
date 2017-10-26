import re
from random import randint
from termcolor import colored
from .timer_controller import TimerController

class ArithmeticController:
    correct_answer_count = 0

    @classmethod
    def start(cls):
        TimerController.start_timer()
        print(colored("スタート!", "green"))
        for i in range(1, 11):
            cls.get_user_answer()
        end_time = TimerController.get_result_time()
        print(colored("\n=> 正解数 : {0}/10, タイム : {1}".format(cls.correct_answer_count, end_time), "green"))

    @classmethod
    def get_user_answer(cls):
        while True:
            problem = cls.create_problem()
            user_answer = input(problem)

            if re.match(r"^[0-9]+$", user_answer):
                if int(user_answer) == cls.correct_answer:
                    cls.correct_answer_count += 1
                    print(colored("◎ 正解!", "yellow"))
                else:
                    print(colored("× 不正解! （正解は{0}）".format(cls.correct_answer), "red"))
                break
            else:
                print(colored("入力された値に誤りがあります", red))

class AdditionController(ArithmeticController):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        cls.correct_answer = num1 + num2
        return "{0:>3d} + {1:>3d} = ".format(num1, num2)

class SubtractionController(ArithmeticController):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 999)
        num2 = randint(num1, 1000)
        cls.correct_answer = num2 - num1
        return "{0:>3d} - {1:>3d} = ".format(num2, num1)

class MultiplicationController(ArithmeticController):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 100)
        num2 = randint(1, 100)
        cls.correct_answer = num2 * num1
        return "{0:>3d} × {1:>3d} = ".format(num1, num2)

class DivisionController(ArithmeticController):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 100)
        # 割り切れる数が見つかるまでループを回す
        while True:
            num2 = randint(num1, 1000)
            if num2 % num1 == 0:
                break
        cls.correct_answer = num2 / num1
        return "{0:>3d} ÷ {1:>3d} = ".format(num2, num1)
