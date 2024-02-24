#!/usr/bin/env python3
from brain_games.games.calc_games import calc_game


def main():
    rounds = input('How many rounds: ')
    calc_game(int(rounds))


if __name__ == '__main__':
    main()
