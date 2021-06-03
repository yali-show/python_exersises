''' HOMEWORK (1) '''
''' 1) Вывести на консоль своё имя, нарисованное 'звёздочками' (I used |; \\ and -)'''
'''i think it is so easy ,so i upgrade my work'''
'''first of all i made variables for colors'''
red = '\033[31m'
yellow = '\033[33m '
blue = '\033[34m '
white = '\033[37m'

'''then i made function for color change'''
# def print_colored_txt(text, color='\033[31m'):
#   print('{} {}'.format(color, text))


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))


'''draw = list()
draw[0] = '----- | |  |  ---'
draw[1] = '  |  |  \\ | |    |'
draw[2] = '  |   |   \\  ----'
draw[3] = '  |   |    | |    |'
draw[4] = '  |   |    | |    |'
draw[5] = '-----   |    | |    |'
'''


''' then i made model of my name and print that with functions'''
out_red('----- | |  |  ---')
out_yellow("  |   |  \\ | |   |")
out_blue('  |   |   \\| -----')
out_red('  |   |    | |   |')
out_yellow('  |   |    | |   |')
out_blue('----- |    | |   |')
