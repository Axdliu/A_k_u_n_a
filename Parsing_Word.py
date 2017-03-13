# -*- coding: utf-8 -*-
"""
1. The count of words in the input
2. the word 'words'
3. each unique word, and count of times in occurs in the input(listedin alphabetical order, each on its own line, with a space between the word and count)
4. the word "letters"
5. for every letter from a to z, the letter, and the count of times that letter occurred IN A WORD
in the input(listed in a alphabetical order, each on its own line, with a space between the letter and count)

@author: User
"""

import string

string_1 = "If the axis is a MultiIndex (hierarchical), count along a particular level, collapsing into a Series"

def parsing_word(string_1):
    
    word = []
    starter = 0
    
    for i in range(len(string_1)):
        if string_1[i] == " " or string_1[i] == "\n":
            word.append(string_1[starter:i])
            starter = i+1
    word.append(string_1[starter:])
    
    real_word =[]
    for w in word:
        lower = 0
        for l in w:
            if l.islower():
                lower +=1
        if lower == len(w):
            real_word.append(w)    
    
    summary = {i:0 for i in list(set(real_word))}    
    for word in real_word:
        summary[word] +=1
    sorted_word = sorted(summary.items(), key = lambda x:x[0])
    
    letter_count = {i:0 for i in string.lowercase[:]} 
    for word in real_word:
        for letter in word:
            letter_count[letter] +=1
    sorted_letter = sorted(letter_count.items(), key = lambda x:x[0])
     
    print len(real_word), '\n', 'words'    
    for word in sorted_word:
        print word[0], word[1]    
    print 'letters'  
    for letter in sorted_letter:
        print letter[0], letter[1]
    
parsing_word(string_1)