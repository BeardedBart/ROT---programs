# Basic ROT-13 alghoritm 
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def input_method():
    word = input('Podaj wyraz do zakodowania: ')
    return word


def encoder_alg(word):

    encoded_word = ''

    for letter in word:
        if letter.lower() in LETTERS:
            position = LETTERS.index(letter.lower())
            
            print(f'Litera: {letter}, pozycja w liście: {position}')
            
            position += 13
            print(f'Nowa pozycja: {position}')

            if position <= 25:
                encoded_letter = LETTERS[position] 
                print(encoded_letter)
                encoded_word += encoded_letter
            else:
                position = position - 26
                #extended_position = 25 - position
                encoded_letter = LETTERS[position] 
                print(encoded_letter)
                encoded_word += encoded_letter
    
    print(f'Zakodowane słowo: {encoded_word}')
    return encoded_word



def main():
    encoder_alg(input_method())

main()