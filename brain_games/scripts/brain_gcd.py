#!/usr/bin/env python3
from brain_games.games.gcd_games import gcd_game


def main():
    rounds = input('How many rounds: ')
    gcd_game(int(rounds))


if __name__ == '__main__':
    main()
