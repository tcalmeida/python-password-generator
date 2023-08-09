import random


def randomize_input(lists, inputs):
    return random.choices(lists, k=inputs)


def create_password_list(lists, empty_list):
    for i in lists:
        empty_list.append(i)


def create_password(password_list):
    password = ""
    for i in password_list:
        password += i
    return password
