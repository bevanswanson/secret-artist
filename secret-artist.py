import os
from random import randint


def get_word():
    with open('random-nouns.txt', 'r') as random_nouns:
        nouns = random_nouns.readlines()
        line_count = len(nouns)
        return nouns[randint(0, line_count)]


def play(player_count, secret_artist, secret_word):
    for current_player in range(1, player_count + 1):
        os.system('clear')
        print(f'you are player {current_player}')
        while True:
            if not input('press ENTER to view your role'):
                if current_player == secret_artist:
                    print('you are the secret artist')
                    print('good luck!')
                else:
                    print('you are NOT the secret artist')
                    print(f'you are drawing: {secret_word.upper()}')
                if current_player != player_count + 1:
                    print('please pass to the next player')
                else:
                    print('you are the last player')
                break

        while input('press ENTER to confirm you have read your instructions'):
            os.system('clear')
            print('press ENTER to confirm you have read your instructions')
        os.system('clear')


def main():
    print('welcome to secret artist!')
    print('*************************')

    while True:
        try:
            player_count = int(input('how many players are there? '))
            break
        except ValueError as err:
            print('you must enter an integer')

    print('OK, thanks!')

    while True:
        if input('are you ready to play? (y/n) ').upper() == 'Y':
            secret_artist = randint(1, player_count)
            secret_word = get_word()
            play(player_count, secret_artist, secret_word)
            break
        else:
            print('OK, nevermind')
            break

    print('thanks for playing secret artist')



if __name__ == '__main__':
    main()
