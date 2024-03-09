# main.py
from dictionary import Dictionary
from operations import add_word, delete_word, update_word

def main():
    my_dictionary = Dictionary()

    while True:
        print("\nDictionary Operations:")
        print("1. Add Word")
        print("2. Delete Word")
        print("3. Update Word")
        print("4. Print Dictionary")
        print("5. Exit")

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            add_word(my_dictionary)
        elif choice == '2':
            delete_word(my_dictionary)
        elif choice == '3':
            update_word(my_dictionary)
        elif choice == '4':
            my_dictionary.print_dictionary()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
