# Basic ROT-13 alghoritm
#
# WARNING! Program can operate only one word yet

LETTERS = list('abcdefghijklmnopqrstuvwxyz')

INCREMENTATION = 2


def input_method():
    word = input('Podaj wyraz do zakodowania: ')
    return word


def encoder_alg(word):

    encoded_word = ''

    for letter in word:
        if letter.lower() in LETTERS:
            position = LETTERS.index(letter.lower())

            print(f'Litera: {letter}, pozycja w liście: {position}')

            position += INCREMENTATION
            print(f'Nowa pozycja: {position}')

            if position <= 25:
                encoded_letter = LETTERS[position]
                print(encoded_letter)
                encoded_word += encoded_letter
            else:
                position = position - 26
                encoded_letter = LETTERS[position]
                print(encoded_letter)
                encoded_word += encoded_letter

    print(f'Zakodowane słowo: {encoded_word}')
    return encoded_word


def decoder_alg(word):

    decoded_word = ''

    for letter in word:
        if letter.lower() in LETTERS:
            position = LETTERS.index(letter.lower())

            print(f'Litera: {letter}, pozycja w liście: {position}')

            position -= INCREMENTATION
            print(f'Nowa pozycja: {position}')

            if position >= 0:
                decoded_letter = LETTERS[position]
                print(decoded_letter)
                decoded_word += decoded_letter
            else:
                position = 26 + position
                decoded_letter = LETTERS[position]
                print(decoded_letter)
                decoded_word += decoded_letter
        if letter == ' ' or letter not in LETTERS:
            decoded_word += letter

    print(f'Zakodowane słowo: {decoded_word}')
    return decoded_word


def save_to_file(file_name, word):
    try:
        fl = open(file_name, 'w+')
    except IOError as e:
        print(f'Nie można otworzyć pliku: {file_name}')
    else:
        fl.write(word)
        fl.close()


def pull_from_file(file_name):
    word = str()
    try:
        fl = open(file_name, 'r')
    except IOError as e:
        print(f'Nie można otworzyć pliku: {file_name}')
    else:
        fl.read(word)
        fl.close
        return word


def main():
    import time
    import sys
    print("""
    Dostępne opcje:
        1) - zakoduj słowo
        2) - odkoduj słowo
    """)
    chose = input('Wybierz opcję: ')

    while chose != '0':
        if chose == '1':
            en_wr = encoder_alg(input_method())  # encoded_word
            save_to_file('encoded.txt', en_wr)
            chose = input('Wybierz opcję: ')

        if chose == '2':
            # decoded_wr = pull_from_file('encoded.txt')
            decoder_alg(
                'yjcv ku vjg pcog qh vjg uauvgo wugf da jco qrgtcvqtu vq ocmg htgg rjqpg ecnnu ?')
            print('Done')
            chose = input('Wybierz opcję: ')


main()
