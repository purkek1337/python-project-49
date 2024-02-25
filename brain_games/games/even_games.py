from brain_games.engine import (welcome_user, game_rules, answer_comparison,
                                generate_question_even)


def even_game():
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[0])  # выводим правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != 3:  # цикл игры
        rounds_counter += 1  # счетчик раундов
        correct_answer = generate_question_even()  # генерируем вопрос
        if answer_comparison(correct_answer, name) == 'wrong':
            break
        if rounds_counter == 3:  # если все ответы верные
            print(f'Congratulations, {name}!')
