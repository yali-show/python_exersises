#made function with loop (for) and if/else
def strange_function(string):
    result = ""
    sl = True  # capitalize
    for letter in string:
        if sl:
            result += letter.lower()
        else:
            result += letter.upper()
        if letter != ' ':
            sl = not sl
    return result
print(strange_function(str(input('Could you pls, write any words:'))))