import numpy as np
import pandas as pd

word = 'abcde'
list_word = [i for i in word]

words_array = []

with open( 'palavars_2.txt', 'r') as f:
    for line in f:
        contents = line.strip().split(',')
        for content in contents:
            word = content[1:6]
            words_array.append(word)

print(words_array)

