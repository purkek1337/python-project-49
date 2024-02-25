from brain_games.engine import (welcome_user, game_rules, answer_comparison, generate_question_gcd)


def gcd_game():
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[2])  # печатаем правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != 3:  # цикл игры
        rounds_counter += 1
        correct_answer = generate_question_gcd()  # генерируем вопрос, возвращаем правильный ответ
        if answer_comparison(correct_answer, name) == 'wrong':  # если неправильно
            break
        if rounds_counter == 3:  # если все ответы верные
            print(f'Congratulations, {name}!')
