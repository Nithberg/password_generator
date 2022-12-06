import random
#test commit
def is_valid(answer):
    yes_or_not = input(answer).lower()
    while True:
        if yes_or_not == 'y' or yes_or_not == 'n':
            break
        else:
            yes_or_not = input('Input is wrong! Please input only "y" for yes or "n" for not! Enter your answer: ')
    return yes_or_not


def get_settings():
    lower = ''.join([chr(c) for c in range(97, 123)])
    upper = ''.join([chr(c) for c in range(65, 91)])
    digits = ''.join([chr(c) for c in range(48, 58)])
    symbols = ''.join([chr(c) for c in range(33, 48)])
    chars_for_pwd = ''
    add_length_pwd = int(input('Add password length: '))
    add_upper_abc = is_valid(
        'Do you want to add uppercase alphabet in your password? (type "y" for yes or "n" for not) ')
    add_lower_abc = is_valid(
        'Do you want to add lowercase alphabet in your password? (type "y" for yes or "n" for not) ')
    add_digits = is_valid('Do you want to add digits in your password? (type "y" for yes or "n" for not) ')
    add_symbols = is_valid('Do you want to add symbols in your password? (type "y" for yes or "n" for not) ')
    if add_upper_abc == 'y':
        chars_for_pwd += upper
    if add_lower_abc == 'y':
        chars_for_pwd += lower
    if add_digits == 'y':
        chars_for_pwd += digits
    if add_symbols == 'y':
        chars_for_pwd += symbols
    return add_length_pwd, chars_for_pwd


def auto_generate_settings():
    chars_for_pwd = ''.join([chr(c) for c in range(97, 123)]) + \
                    ''.join([chr(c) for c in range(65, 91)]) + \
                    ''.join([chr(c) for c in range(48, 58)]) + \
                    ''.join([chr(c) for c in range(33, 48)])
    add_length_pwd = int(input('Add password length: '))

    return add_length_pwd, chars_for_pwd


def generate_password(length, chars):
    pwd = ''
    for i in range(length):
        pwd += random.choice(chars)
    return pwd


def main():
    setting_generator = input(
        'Do you want to use automatic password generation settings or advanced? (type "auto" or "manual") ')
    if setting_generator == 'manual':
        add_number = int(input('Add number of password to generate: '))
        length, chars = get_settings()
        for i in range(add_number):
            print(f'{generate_password(length, chars)} - password {i + 1}')
        return

    if setting_generator == 'auto':
        add_number = int(input('Add number of password to generate: '))
        length, chars = auto_generate_settings()
        for i in range(add_number):
            print(f'{generate_password(length, chars)} - password {i + 1}')
        return


main()
