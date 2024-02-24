import prompt
from random import randint


game_rules = ('Answer "yes" if the number is even, '
              'otherwise answer "no".',
              'What is the result of the expression?')


def welcome_user():  # функция приветствия
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):  # функция проверки чётности числа
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def answer_comp(correct_answer, name):  # функция сравнения ответов
    user_answer = input('Your answer: ')
    if str(correct_answer) == user_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return 'wrong'


def generate_question_even():  # функция генерации вопроса even_games
    number = randint(1, 100)  # генерация вопроса
    print(f'Question: {number}')
    return number


def generate_question_calc():
    operators = ('+', '-', '*')  # генерация вопроса
    operator = operators[randint(0, 2)]
    a = randint(1, 100)
    b = randint(1, 100)
    if operator == '+':
        print(f'Question: {a} + {b}')
        correct_answer = a + b
        return correct_answer
    elif operator == '-':
        print(f'Question: {a} - {b}')
        correct_answer = a - b
        return correct_answer
    else:
        print(f'Question: {a} * {b}')
        correct_answer = a * b
        return correct_answer
