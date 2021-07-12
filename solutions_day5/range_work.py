'''
****************************************************
function calculate range of even numbers
****************************************************
x , y - int values
x must be less than y
return: list of even numbers placed between x and y
'''


def even_numbers_range(x, y):
    first_number_in_range = x
    last_number_in_range = y
    step = 2

    # to check if first number is odd we can skip it
    # in our next constructions our range started i made first number as even
    # it gave me possibility to make step equal 2
    if first_number_in_range % 2 != 0:
        first_number_in_range += 1

    numbers_in_range = list(range(first_number_in_range, last_number_in_range, step))

    return(numbers_in_range)

if __name__ == '__main__':
    first_number = int(input('First number: '))
    last_number = int(input('Last number: '))
    print(even_numbers_range(first_number, last_number))
