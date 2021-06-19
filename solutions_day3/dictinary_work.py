def get_statistic(word):
    element_stat = {}

    for letter in word:
        counter = word.count(letter)
        if letter not in element_stat:
            element_stat[letter] = counter

    return element_stat


if __name__ == '__main__':
    word = str(input('Write your word to dict that: '))
    print(get_statistic(word))
