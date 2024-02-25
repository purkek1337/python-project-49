#!/usr/bin/env python3
from brain_games.games.prime_games import prime_game


def main():
    rounds = input('How many rounds: ')
    prime_game(int(rounds))


if __name__ == '__main__':
    main()
