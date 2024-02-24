from brain_games.engine import (welcome_user, game_rules, is_even, answer_comp,
                                generate_question_even)


def even_game(rounds):
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[0])  # выводим правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != rounds:  # цикл игры
        rounds_counter += 1  # счетчик раундов
        correct_answer = is_even(generate_question_even())  # правильный ответ
        if answer_comp(correct_answer, name) == 'wrong':  # если неправильно
            break
        if rounds_counter == rounds:  # если все ответы верные
            print(f'Congratulations, {name}!')
