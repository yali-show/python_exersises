def make_string(word) -> str:
    if len(word) % 2 == 0:
        first_element = (len(word) // 2) - 1
        second_element = (len(word) // 2) + 1
        #because slice work ([1:3] in this example) from 1 to 3 (3 not included)4
        word = word[first_element:second_element]
    else:
        first_element = (len(word) // 2) - 1
        third_element = (len(word) // 2) + 2
        word = word[first_element:third_element]

    return word


if __name__ == '__main__':
    your_string = str(input('Write your word: '))
    print(make_string(your_string))
