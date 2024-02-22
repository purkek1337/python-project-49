import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def is_even(number):  # функция проверки чётности числа
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'
