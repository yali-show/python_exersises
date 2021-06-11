#made function with loop (for) and if/else
def modefy_string(string):
    result = ""
    is_char = True  # capitalize
    for letter in string:
        if is_char:
            result += letter.lower()
        else:
            result += letter.upper()
        if letter != ' ':
            is_char = not is_char
    return result
#print(modefy_string(str(input('Could you pls, write any words:'))))


def stranger_string(string):
    splited_string = string.split()
    str = ""
    for element in splited_string:
        for i in range(len(element)):

            if i % 2 == 1:          # is it odd
                str = str + element[i].upper()
            else:
                str = str + element[i]
    return str
if __name__ == '__main__':
    print(stranger_string(str(input('Type your sentence: '))))