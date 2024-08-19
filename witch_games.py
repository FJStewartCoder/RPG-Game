import random as r
from time import sleep


def rock_paper_scissors(amount_of_games=1, computer_name='Computer'):
    computer_wins = 0
    player_wins = 0

    for _ in range(amount_of_games):
        options = ['rock', 'paper', 'scissors']
        computer_choice = r.choice(options)
        print('Rock, Paper, Scissors')
        while True:
            player_choice = input('>>> ').lower()
            if player_choice not in options:
                print('Try again.')
            break

        print(f'You picked {player_choice}.')
        print(f'{computer_name} picked {computer_choice}.\n')
        sleep(3)

        play = [player_choice, computer_choice]
        play.sort()

        if player_choice == computer_choice:
            print('Draw.')

        elif play == ['paper', 'rock']:
            if player_choice == 'paper':
                print('You win.')
                player_wins += 1
            else:
                print('You lose.')
                computer_wins += 1

        elif play == ['paper', 'scissors']:
            if player_choice == 'scissors':
                print('You win.')
                player_wins += 1
            else:
                print('You lose.')
                computer_wins += 1

        else:
            if player_choice == 'rock':
                print('You win.')
                player_wins += 1
            else:
                print('You lose.')
                computer_wins += 1

    if computer_wins == player_wins:
        print('Overall, you draw.')
        return False
    elif computer_wins > player_wins:
        print(f'Overall, {computer_name} wins.')
        return False
    else:
        print('Overall, you win.')
        return True


def dice_game(amount_of_games=1, computer_name='Computer'):
    computer_wins = 0
    player_wins = 0

    for _ in range(amount_of_games):
        computer_roll = r.randint(1, 6) + r.randint(1, 6)
        player_roll = r.randint(1, 6) + r.randint(1, 6)

        sleep(2)

        print(f'You rolled {player_roll}.')
        print(f'{computer_name} rolled {computer_roll}.')

        sleep(3)

        if computer_roll == player_roll:
            print('You draw.\n')
        elif computer_roll > player_roll:
            print('You lose.\n')
            computer_wins += 1
        else:
            print('You win.\n')
            player_wins += 1

    if computer_wins == player_wins:
        print('Overall, you draw.')
        return False
    elif computer_wins > player_wins:
        print(f'Overall, {computer_name} wins.')
        return False
    else:
        print('Overall, you win.')
        return True


if __name__ == '__main__':
    dice_game(5)
    rock_paper_scissors(5)
