#!/usr/bin/env python

from random import randint
from brain_games.brain_games_logic import game_cycle, welcome_user, rules


def result_checker(n):

    i = 2
    while(i < n):
        if (n % i == 0):
            result = 'no'
            break
        else:
            result = 'yes'
        i = i + 1
    return result


def game():

    name = welcome_user()
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    rules(rule)

    i = 0
    while (i < 3):
        rand_int = randint(1, 100)

        question = str(rand_int)
        correct_answer = result_checker(rand_int)

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
