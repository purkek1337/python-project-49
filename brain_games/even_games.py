from random import randint
from brain_games.cli import welcome_user


def is_even(number): # функция проверки чётности числа
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even_game():
    name = welcome_user() # выполняем приветствие и возвращаем имя
    print('Answer "yes" if the number is even, otherwise answer "no".') # правила игры
    for i in range(3): # в игре 3 раунда
        number = randint(1, 100) # создаем переменную рандомного числа
        print(f'Question: {number}') # выводим вопрос
        user_answer = input('Your answer: ') # вводим ответ
        if is_even(number) == user_answer: # сравниваем вопрос с ответом
            print('Correct!') # верный ответ
        else: # неверный ответ
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{is_even(number)}'")
            print(f"Let's try again, {name}!")
            return # программа закрывается
    print(f'Congratulations {name}!') # при трёх правильных ответах игрок побеждает
