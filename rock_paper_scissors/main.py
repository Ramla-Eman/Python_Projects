import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK: '✊', PAPER: '📃', SCISSORS: '✂'}
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user = input(
            f"What's your choice? {ROCK} for Rock, {PAPER} for Paper, {SCISSORS} for Scissors: ").lower()

        if user in choices:
            return user
        else:
            print('Invalid Choice')


def show_choices(user, computer):
    print(f'you choose {emojis[user]}')
    print(f'computer choose {emojis[computer]}')


def is_win(user, computer):
    if user == computer:
        return f"It's a Draw!"
    elif (
        (user == ROCK and computer == SCISSORS) or
        (user == SCISSORS and computer == PAPER) or
        (user == PAPER and computer == ROCK)
    ):
        print(f"You Won!")
    else:
        print('You Lose')


def play():
    while True:
        user = get_user_choice()

        computer = random.choice(choices)

        show_choices(user, computer)
        is_win(user, computer)

        should_continue = input('continue (y/n): ').lower()
        if should_continue == 'n':
            break


play()
