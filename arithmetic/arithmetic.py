from random import randint
import re

class Arithmetic:
    correct_answer_count = 0

    @classmethod
    def start(cls):
        for i in range(1, 11):
            cls.get_user_answer()
        print("結果 : {0}/10".format(cls.correct_answer_count))

    @classmethod
    def get_user_answer(cls):
        while True:
            problem = cls.create_problem()
            user_answer = input(problem)

            if re.match(r"^[0-9]+$", user_answer):
                if int(user_answer) == cls.correct_answer:
                    cls.correct_answer_count += 1
                    print("正解")
                    break
                else:
                    print("不正解")
                    break
            else:
                print("入力された値に誤りがあります")

class Addition(Arithmetic):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 1000)
        num2 = randint(1, 1000)
        cls.correct_answer = num1 + num2
        return "{0:>3d} + {1:>3d} = ".format(num1, num2)

class Subtraction(Arithmetic):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 999)
        num2 = randint(num1, 1000)
        cls.correct_answer = num2 - num1
        return "{0:>3d} - {1:>3d} = ".format(num2, num1)

class Multiplication(Arithmetic):
    @classmethod
    def create_problem(cls):
        num1 = randint(1, 99)
        num2 = randint(1, 99)
        cls.correct_answer = num2 * num1
        return "{0:>3d} × {1:>3d} = ".format(num1, num2)

class Division(Arithmetic):
    @classmethod
    def create_problem(cls):
        while True:
            num1 = randint(1, 100)
            num2 = randint(num1, 1000)
            if num2 % num1 == 0:
                break
        cls.correct_answer = num2 / num1
        return "{0:>3d} ÷ {1:>3d} = ".format(num2, num1)
