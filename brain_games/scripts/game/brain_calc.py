#!/usr/bin/env python

from random import randint
from brain_games.brain_games_logic import game_cycle, welcome_user, rules


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

    return str(result)


def game():

    name = welcome_user()
    rule = 'What is the result of the expression?'
    rules(rule)

    i = 0
    while (i < 3):
        first_rand_int = randint(1, 100)
        second_rand_int = randint(1, 100)

        operator = operator_generator()
        question = str(first_rand_int) + ' ' + operator + ' ' + \
            str(second_rand_int)

        correct_answer = result_checker(first_rand_int,
                                        second_rand_int, operator)
        correctness_of_user_answer = game_cycle(question,
                                                correct_answer, name)

        if (correctness_of_user_answer):
            i = i + 1
        else:
            return
    print('Congratulations, ' + name + '!')


def main():
    game()


if __name__ == '__main__':
    main()
