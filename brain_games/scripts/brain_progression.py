#!/usr/bin/env python3
from brain_games.games.progression_games import progression_game


def main():
    rounds = input('How many rounds: ')
    progression_game(int(rounds))


if __name__ == '__main__':
    main()
