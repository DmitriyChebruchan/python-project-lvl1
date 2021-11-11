#!/usr/bin/env python

from random import randint
from brain_games.brain_games_logic import game_cycle, welcome_user, rules


def result_checker(first_number, second_number):

    result = 1

    max = first_number
    if first_number > second_number:
        max = second_number

    i = 1
    while (i < max + 1):
        if((first_number % i == 0) and (second_number % i == 0)):
            result = i
        i = i + 1
    return str(result)


def game():

    rule = 'Find the greatest common divisor of given numbers.'

    name = welcome_user()
    rules(rule)

    i = 0
    while (i < 3):
        first_rand_int = randint(1, 100)
        second_rand_int = randint(1, 100)

        question = str(first_rand_int) + ' ' + str(second_rand_int)
        correct_answer = result_checker(first_rand_int,
                                        second_rand_int)
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
