#!/usr/bin/env python

from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def rules():

    print('Answer "yes" if the number is even, otherwise answer "no".')


def num_checker(n):

    if n % 2 == 0:
        return 'yes'
    else:
        return 'no'


def answer_puller(rand_number):
    answer = prompt.string('Question: ' + str(rand_number) + '\nYour answer:')
    return answer


def answer_checker(answer, correct_answer):

    if (answer != 'yes' and answer != 'no'):
        return False

    if answer == correct_answer:
        return True
    else:
        return False


def response_generator(corretness_of_user_answer, correct_answer,
                       user_answer, name):

    responce = ''
    correct_y_n = ''

    if (corretness_of_user_answer):
        responce = 'Correct!'
        print(responce)
        return
    elif correct_answer is True:
        correct_y_n = 'yes'
    elif correct_answer is False:
        correct_y_n = 'no'
    else:
        correct_y_n = correct_answer

    responce = "'" + user_answer + "' is wrong answer;(\
. Correct answer was '" + correct_y_n + "'\nLet\'s try again, " + name + "!"
    print(responce)


def game_cycle():

    name = welcome_user()
    rules()
    i = 0
    while (i < 3):

        rand_number = randint(1, 100)
        checked_num = num_checker(rand_number)
        answer = answer_puller(rand_number)
        correctness_of_user_answer = answer_checker(answer, checked_num)

        response_generator(correctness_of_user_answer,
                           checked_num, answer, name)

        if (correctness_of_user_answer):
            i = i + 1
        else:
            i = 0
    print('Congratulations, ' + name + '!')


def main():
    game_cycle()


if __name__ == '__main__':
    main()
