from brain_games.engine import (welcome_user, game_rules, answer_comparison,
                                generate_question_prime)


def prime_game(rounds):
    name = welcome_user()  # выполняем приветствие и возвращаем имя
    print(game_rules[4])  # печатаем правила
    rounds_counter = 0  # счетчик раундов
    while rounds_counter != rounds:
        rounds_counter += 1
        correct_answer = generate_question_prime()
        if answer_comparison(correct_answer, name) == 'wrong':  # если неправильно
            break
        if rounds_counter == rounds:  # если все ответы верные
            print(f'Congratulations, {name}!')
