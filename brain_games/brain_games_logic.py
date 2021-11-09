#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def rules(rule):
    print(rule)


def answer_puller(generated_question):
    answer = prompt.string('Question: ' + generated_question + '\nYour answer:')

    return answer


def answer_checker(correct_answer, user_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def response_generator(corretness_of_user_answer, correct_answer,
                       user_answer, name):

    responce = ''

    if (corretness_of_user_answer):
        responce = 'Correct!'
    else:
        responce = "'" + str(user_answer) + "' is wrong answer;(\
.Correct answer was '" + str(correct_answer) + "'\n\
Let\'s try again, " + name + "!"
    print(responce)


def game_cycle(rule, question, correct_answer, name):

    user_answer = answer_puller(question)
    correctness_of_user_answer = answer_checker(correct_answer, user_answer)
    response_generator(correctness_of_user_answer,
                       correct_answer, user_answer, name)

    return correctness_of_user_answer
