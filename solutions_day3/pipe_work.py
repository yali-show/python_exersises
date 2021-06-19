def splited_string(given_marks) -> dict:
    my_dicty = {}

    for element in given_marks:
        split_string = element.split('|')
        my_dicty[split_string[0]] = split_string[1].split(',')

    for key in my_dicty:
        values = my_dicty[key]
        striped_values = []
        for value in values:
            striped_values.append(value.strip())
        my_dicty[key] = striped_values

    return my_dicty


def averged_result(my_dicty) -> dict:
    my_dictionary = {}

    for key in my_dicty:
        values = my_dicty[key]
        numbers = list(map(int, values)) #applyed map to covert str to int
        my_dictionary[key] = sum(numbers) / len(values)

    return my_dictionary

def convert(dict_to_convert) -> list:
    result = []

    for key in dict_to_convert:
        value = dict_to_convert[key]
        result.append('{}|{}'.format(key, value))

    return result


if __name__ == '__main__':
    marks = ["Mike|83,90,1,20", "Rayan|12,34,56", "Jane|45,46,31,33"]
    dictionary = splited_string(marks)
    print(convert(averged_result(dictionary)))