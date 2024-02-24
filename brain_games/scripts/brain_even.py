#!/usr/bin/env python3
from brain_games.games.even_games import even_game


def main():
    rounds = input('How many rounds: ')
    even_game(int(rounds))


if __name__ == '__main__':
    main()
