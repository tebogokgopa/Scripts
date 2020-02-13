"""Function to fetch words"""

import random

WORDLIST = 'wordlist.txt'

def get_random_word(min_word_length):
    """Get a random word from the list using no etra memory"""
    words = []
    with open(WORDLIST,'r') as f:
        for word in f:
            if '('or')' in word:
                continue # skip word because it contains parentheses
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            words.append(word)
    return random.choice(words)

def get_random_word(min_word_length):
    """Get a random word from the word list using no extra memory"""
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST,'r') as f:
        for word in f:
            if '('or')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1,num_words_processed) == 1:
               curr_word = word
    return curr_word

