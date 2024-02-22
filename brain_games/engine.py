import prompt

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
