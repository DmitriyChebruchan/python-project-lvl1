#!/usr/bin/env python

from random import randint

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def rules():

    print('What is the result of the expression?')


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

    result = ''

    if operator == '+':
        result = str(first_number + second_number)
    elif operator == '-':
        result = str(first_number - second_number)
    elif operator == '*':
        result = str(first_number * second_number)
    return result


def answer_puller(first_rand_int, second_rand_int, operator):

    answer = prompt.string('Question: ' + str(first_rand_int) +
                           str(operator) + str(second_rand_int) +
                           '\nYour answer:')

    return answer


def answer_checker(answer, correct_answer):

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
.Correct answer was '" + correct_y_n + "'\nLet\'s try again, " + name + "!"
    print(responce)


def game_cycle():

    name = welcome_user()
    rules()
    i = 0
    while (i < 3):

        first_rand_int = randint(1, 100)
        second_rand_int = randint(1, 100)
        operator = operator_generator()

        checked_num = result_checker(first_rand_int, second_rand_int, operator)
        answer = answer_puller(first_rand_int, second_rand_int, operator)
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
