def even_numbers_range(x, y):
    first_number_in_range = x + 1
    last_number_in_range = y
    numbers_in_range = list(range(first_number_in_range, last_number_in_range))
    even_numbers_in_range = []
    for number in numbers_in_range:
        if number % 2 == 0:
            even_numbers_in_range.append(number)
    return(even_numbers_in_range)

if __name__ == '__main__':
    first_number = int(input('First number: '))
    last_number = int(input('Last number: '))
    print(even_numbers_range(first_number, last_number))