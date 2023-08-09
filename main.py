import random
from generate_pass import randomize_input, create_password_list, create_password

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'K', 'L', 'M', 'N', 'O', 'P']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']


def main():
    print('---Creating password---')
    inp_letters = int(input('choose letter quantity: '))
    inp_numbers = int(input('choose number quantity: '))
    inp_symbols = int(input('choose symbol quantity: '))

    password_list = []

    rand_letters = randomize_input(letters, inp_letters)
    rand_numbers = randomize_input(numbers, inp_numbers)
    rand_symbols = randomize_input(symbols, inp_symbols)

    create_password_list(rand_letters, password_list)
    create_password_list(rand_numbers, password_list)
    create_password_list(rand_symbols, password_list)




if __name__ == '__main__':
    main()
