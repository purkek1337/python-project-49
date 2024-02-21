from random import randint
from brain_games.cli import welcome_user


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        user_answer = input('Your answer: ')
        if is_even(number) == user_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{is_even(number)}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations {name}!')
