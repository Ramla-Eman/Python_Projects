import random

def play():
    user = input(f"What's your choice? 'r' for rock, 'p' for Paper 's' for Scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'It\'s a Draw ! Try Again'
    
    if is_win(user, computer):
        return f'You Won! Computer chose {computer}'
    else:
        return f'Computer Won! Computer chose {computer}'


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())