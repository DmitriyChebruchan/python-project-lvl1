#!/usr/bin/env python

from random import randint
from brain_games.brain_games_logic import game_cycle, welcome_user, rules


def result_checker(first_int, total_quantity, missing_int, step):

    if missing_int == 1:
        result = first_int
    else:
        result = first_int + missing_int * step

    return str(result)


def sequence_generator(first_int, total_quantity, missing_int, step):
    result = ''

    i = 0
    while (i < total_quantity):
        if i == 0:
            if missing_int != 0:
                result = str(first_int) + ' '
            else:
                result = '.. '
        else:
            if i == missing_int:
                result = str(result + '.. ')
            else:
                result = str(result + str(first_int + i * step) + ' ')
        i = i + 1
    return result


def game():

    name = welcome_user()
    rule = 'What is the result of the expression?'
    rules(rule)

    i = 0
    while (i < 3):
        first_int = randint(1, 100)
        total_quantity = randint(5, 10)
        missing_int = randint(0, total_quantity - 1)
        step = randint(1, 10)

        question = sequence_generator(first_int, total_quantity,
                                      missing_int, step)

        correct_answer = result_checker(first_int, total_quantity,
                                        missing_int, step)

        correctness_of_user_answer = game_cycle(question,
                                                correct_answer, name)

        if (correctness_of_user_answer):
            i = i + 1
        else:
            i = 0

    print('Congratulations, ' + name + '!')


def main():
    game()


if __name__ == '__main__':
    main()
