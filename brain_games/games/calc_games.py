from brain_games.engine import (welcome_user, game_rules, answer_comparison,
                                generate_question_calc)


def calc_game():
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[1])  # печатаем правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != 3:
        rounds_counter += 1
        correct_answer = generate_question_calc()
        if answer_comparison(correct_answer, name) == 'wrong':
            break
        if rounds_counter == 3:  # если все ответы верные
            print(f'Congratulations, {name}!')
