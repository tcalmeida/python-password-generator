import random
from chars import letters, numbers, symbols
from generate_pass import randomize_input, create_password_list, create_password


def main():
    print('---Creating password---')
    inp_letters = int(input('choose letter quantity: '))
    inp_numbers = int(input('choose number quantity: '))
    inp_symbols = int(input('choose symbol quantity: '))

    password_list = []

    # choose random char from lists
    rand_letters = randomize_input(letters, inp_letters)
    rand_numbers = randomize_input(numbers, inp_numbers)
    rand_symbols = randomize_input(symbols, inp_symbols)

    # add random char in password list
    create_password_list(rand_letters, password_list)
    create_password_list(rand_numbers, password_list)
    create_password_list(rand_symbols, password_list)

    random.shuffle(password_list)

    password = create_password(password_list)

    print(f'Your password is: {password}')


if __name__ == '__main__':
    main()
