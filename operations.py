# operations.py
from dictionary import Dictionary

def add_word(dictionary):
    word = input('Enter the word: ')
    meaning = input('Enter the meaning: ')
    dictionary.add_word(word, meaning)

def delete_word(dictionary):
    word = input('Enter the word to delete: ')
    dictionary.delete_word(word)

def update_word(dictionary):
    word = input('Enter the word to update: ')
    new_meaning = input('Enter the new meaning: ')
    dictionary.update_word(word, new_meaning)
