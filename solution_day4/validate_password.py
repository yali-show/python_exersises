def validate_char(password):
    message = []


    ZERO_IN_ASCI = 48
    EIGHT_IN_ASCI = 57
    UPPER_A_IN_ASCI = 65
    UPPER_Z_IN_ASCI = 90
    LOWER_A_IN_ASCI = 97
    LOWER_Z_IN_ASCI = 122

    for char in password:
        char_orded = ord(char)
        if char_orded < ZERO_IN_ASCI or EIGHT_IN_ASCI < char_orded:      #numbers

           if char_orded < UPPER_A_IN_ASCI or UPPER_Z_IN_ASCI < char_orded:   #letters in upper

               if char_orded < LOWER_A_IN_ASCI  or  LOWER_Z_IN_ASCI < char_orded:            #letters in lower
                   message = [" содержит запрещенные символы"]
    return message


def odd_number_count(password):
   message = []
   number_list = []
   list_char = password.split()

   for number in password:
       if number.isdigit():
           number_list.append(number)

   number_count = len(number_list)

   if number_count % 2 == 0:
        error = 'введено парное количесвто цыфр'
        message.append(error)

   return message

def even_letter_count(password):
    message = []
    letters_list = []
    for letter in password:
        if letter.isalpha():
            letters_list.append(letter)

    letter_count = len(letters_list)

    if letter_count % 2 != 0:
        error = 'введено непарное количсество букв'
        message.append(error)

    return message


def validate_password(password):
    res_validate_char     = validate_char(password)
    res_odd_number_count  = odd_number_count(password)
    res_even_letter_count = even_letter_count(password)
    result = res_validate_char + res_odd_number_count + res_even_letter_count
    return result


if __name__ == '__main__':
    your_password = input('Введи пароль: ')
    print(validate_password(your_password))

