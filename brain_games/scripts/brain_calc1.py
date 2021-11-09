#!/usr/bin/env python

from random import randint
from brain_games.brain_games_logic import *


def operator_generator():

    result = ''
    rand_operator_int = randint(1, 3)

    if (rand_operator_int == 1):
        result = '+'
    elif (rand_operator_int == 2):
        result = '-'
    else:
        result = '*'

    return result


def result_checker(first_number, second_number, operator):

    result = 0

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number

    return result


rules = 'What is the result of the expression?'

first_rand_int = randint(1, 100)
second_rand_int = randint(1, 100)

operator = operator_generator()
question = str(first_rand_int) + operator + str(second_rand_int)
correct_answer = result_checker(first_rand_int, second_rand_int, operator)


def main():

    game_cycle(rules, question, correct_answer)


if __name__ == '__main__':
    main()
