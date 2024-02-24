from brain_games.engine import (welcome_user, game_rules, answer_comp, generate_question_gcd)


def gcd_game(rounds):
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[2])  # печатаем правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != rounds:
        rounds_counter += 1
        correct_answer = generate_question_gcd()
        if answer_comp(correct_answer, name) == 'wrong':  # если неправильно
            break
        if rounds_counter == rounds:  # если все ответы верные
            print(f'Congratulations, {name}!')