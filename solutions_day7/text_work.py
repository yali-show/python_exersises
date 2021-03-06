def text_work(file):
    '''

    file   - name of file.txt
    return - dictionary of words
    '''
    message_smile = '\U0001F61F'
    error_smile = '\N{FEARFUL FACE}'
    try:
        with open(file, "r") as initial_text:
            initial_text = initial_text.read()
            initial_text = initial_text.replace("!", "")\
                .replace(".", "")\
                .replace(",", "")\
                .replace("?", "")\
                .replace("'", "")\
                .replace('"', "")\
                .replace('-', "")\
                .replace('*', "")\
                .replace(';', "")\
                .replace(':', "")\
                .replace('(', "")\
                .replace(')', "")

            dict_of_words = {}
            initial_text = initial_text.split()
            for word in initial_text:
                count = initial_text.count(word)
                dict_of_words[word] = count

        return dict_of_words

    except Exception:
        print(message_smile + "something wrong" + message_smile)
        return 'Error' + error_smile

if __name__ == '__main__':
    text_file = r'book-war-and-peace.txt'
    print(text_work(text_file))
