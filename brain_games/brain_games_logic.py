#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name


def rules(rules):
    print(rules)


def answer_puller(generated_question):
    answer = prompt.string('Question: ' + generated_question + '\nYour answer:')

    return answer


def answer_checker(user_answer, correct_answer):

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
        responce = "'" + user_answer + "' is wrong answer;(\
.Correct answer was '" + correct_answer + "'\n\
Let\'s try again, " + name + "!"
    print(responce)


def game_cycle(rules, generated_question, correct_answer):

    name = welcome_user()
    rules(rules)

    i = 0
    while (i < 3):

        user_answer = answer_puller(generated_question)
        correctness_of_user_answer = answer_checker(correct_answer, user_answer)
        response_generator(correctness_of_user_answer,
                           correct_answer, user_answer, name)

        if (correctness_of_user_answer):
            i = i + 1
        else:
            i = 0
    print('Congratulations, ' + name + '!')
