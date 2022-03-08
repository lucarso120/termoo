import pandas as pd
import numpy as np

from boxit.boxit import boxit
import random



words_array = []

with open( 'palavars_2.txt', 'r') as f:
    for line in f:
        contents = line.strip().split(',')
        for content in contents:
            word = content[1:6]
            words_array.append(word)

all_words = words_array
all_words_2 = np.array(words_array)


    
def select_word():
    word = random.choice(all_words)
    return word

def select_word_specific(lista):
    word = random.choice(lista)
    return word


def play_game():
    table = [['⬜' for y in range(5)] for x in range(6) ] 
    attempts = 0
    word = select_word()
    print(word, '\n')
    board = ['_'] * 5
    possible_words = np.array(all_words)
    
    
    while attempts < 5:

        guess = select_word_specific(possible_words)
        correct = False
        

        if len(guess) != 5:
            print('The word must have 5 letters')
            attempts -= 1 #neutralize # of attempts
            break

        #this works for+ placing the letters
        for index in range(len(guess)):
            if guess[index] in word:
                # board[letter] = '0'
                table[attempts][index] = '🟨'
                
                for item in possible_words:
                    if guess[index] not in item:
                        possible_words = possible_words[possible_words != item]

            if guess[index] == word[index]:
                table[attempts][index] = '🟩'
                letter = guess[index]
                for item in possible_words:
                    if letter not in item[index]:
                        possible_words = possible_words[possible_words != item]

                        
                #proximo passo: desconsiderar letras que nao estão
            if guess[index] not in word:
                for item in possible_words:
                    if guess[index] in item:
                        possible_words = possible_words[possible_words != item]
        possible_words = possible_words[possible_words != guess]
        print(table[attempts])
        print(guess)

        if guess == word:
            print("you won!")
            return True
            break

        attempts += 1
        board = ['_'] * 5

play_game()



