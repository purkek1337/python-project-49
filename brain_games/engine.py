import prompt
from random import randint, choice


game_rules = ('Answer "yes" if the number is even, '
              'otherwise answer "no".',
              'What is the result of the expression?',
              'Find the greatest common divisor of given numbers.',
              'What number is missing in the progression?')

"""
Game rules:
    0 - even_games
    1 - calc_games
    2 - gcd_games
    3 - progression_games
"""


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


def answer_comparison(correct_answer, name):  # функция сравнения ответов
    user_answer = input('Your answer: ')
    if str(correct_answer) == user_answer:
        print('Correct!')
    else:
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return 'wrong'


def generate_question_even():  # генерации вопроса even_games
    random_number = randint(1, 100)
    correct_answer = is_even(random_number)
    print(f'Question: {random_number}')
    return correct_answer


def generate_question_calc():  # генерация вопроса calc_games
    correct_answer = ''
    operator = choice(('+', '-', '*'))
    a = randint(1, 100)
    b = randint(1, 100)

    match operator:
        case '+':
            print(f'Question: {a} + {b}')
            correct_answer = a + b
        case '-':
            print(f'Question: {a} - {b}')
            correct_answer = a - b
        case '*':
            print(f'Question: {a} * {b}')
            correct_answer = a * b

    return correct_answer


def generate_question_gcd():  # генерации вопроса gcd_games
    a = randint(1, 100)
    b = randint(1, 100)

    print(f'Question: {a} {b}')

    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


def generate_question_progression():
    progression = []
    random_index = randint(1, 10)

    for i in range(1, 150, randint(2, 10)):
        if len(progression) == 10:
            break
        else:
            progression.append(i)

    correct_answer = progression[random_index]

    progression[random_index] = '..'
    progression_question = 'Question:', *progression

    print(*progression_question)
    return correct_answer
