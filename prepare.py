from random import choice
import pathlib
with open('freqrnc2011.csv', 'r', encoding='utf-8') as f:
    f.readline()
    data = f.read().splitlines()
wordlist = []
for line in data:
    new_line = line.split('\t', maxsplit=2)
    if new_line[1] == 's':
        wordlist.append(new_line[0])
t = 1
with open('hangman.txt', 'r', encoding='utf-8') as f:
    picture = f.readlines()
    for i, symbol in enumerate(picture):
        if symbol != '\n':
            file = pathlib.Path('{}.txt'.format(t)).open('a')
            file.write(f'{picture[i]}')
            file.close()
        elif symbol == '\n' and picture[i+1] == '\n':
            t += 1
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = choice(wordlist)
number_of_guesses = []
example = '_' * len(word)
lst_example = list(example)
j = 1
print(f'Я загадал слово из {len(word)} букв.\n{example}')
while True:
    if '_' in lst_example:
        guess = input('Введите букву: ')
        guess = guess.lower()
        if guess in alphabet:
            if guess in number_of_guesses:
                print('Вы уже вводили эту букву. Введите другую')
            else:
                while guess in word:
                    for i, letter in enumerate(word):
                        if letter == guess:
                            lst_example[i] = guess
                        else:
                            pass
                    print(''.join(lst_example))
                    break
                else:
                    number_of_guesses.append(guess)
                    if len(number_of_guesses) == 9:
                        with open('10.txt', 'r', encoding='utf-8') as pu:
                            print(f'Вы лох - игра окончена. Загаданное слово - {word}\n{pu.read()}')

                        break
                    else:
                        with open('{}.txt'.format(j), 'r', encoding='utf-8') as risunok:
                            print(f'ты бомж, осталось попыток - {9 - len(number_of_guesses)}\n{risunok.read()}')
                            j += 1
        else:
            print('Введите нормальную букву')
    else:
        print('Вы выиграли!')
        break
