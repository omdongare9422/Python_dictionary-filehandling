# dictionary.py

import json

class Dictionary:
    def __init__(self, file_path="dictionary.json"):
        self.file_path = file_path
        self.words = self.load_dictionary()

    def load_dictionary(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_dictionary(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.words, file, indent=2)

    def add_word(self, word, meaning):
        self.words[word] = meaning
        self.save_dictionary()
        print(f'Word "{word}" added successfully.')

    def delete_word(self, word):
        if word in self.words:
            del self.words[word]
            self.save_dictionary()
            print(f'Word "{word}" deleted successfully.')
        else:
            print(f'Word "{word}" not found in the dictionary.')

    def update_word(self, word, new_meaning):
        if word in self.words:
            self.words[word] = new_meaning
            self.save_dictionary()
            print(f'Meaning of "{word}" updated successfully.')
        else:
            print(f'Word "{word}" not found in the dictionary.')

    def print_dictionary(self):
        print("Dictionary:")
        for word, meaning in self.words.items():
            print(f'{word}: {meaning}')
