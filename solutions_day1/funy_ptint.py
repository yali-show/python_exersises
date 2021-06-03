import random
''' HOMEWORK (1) '''
''' 1) Вывести на консоль своё имя, нарисованное 'звёздочками' (I used |; \\ and -)'''
'''FIRST VARIANT'''

def out_red(text):
    '''
    outy_red - color my message in red
    :param text: any text you want to print
    '''
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))



'''pseudographics to print my name'''
out_red('----- | |  |  ---')
out_yellow("  |   |  \\ | |   |")
out_blue('  |   |   \\| -----')
out_red('  |   |    | |   |')
out_yellow('  |   |    | |   |')
out_blue('----- |    | |   |')

'''SECOND VARIANT'''
''' made variables for colors'''
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
white = '\033[37m'


def color_txt(txt, color='\033[31m'):
    '''
    :param txt: text you want to paint
    :param color: code of color (by defolt red)
    '''
    print("{} {}".format(txt, color))

'''made lists for colors and graphics'''
colors = [red, yellow, blue, white]
lines = list()
lines.append('----- | |  |  ---')      #  .append - add to the tail of list
lines.append('  |   |  \\ | |   |')
lines.append('  |   |   \\| -----')
lines.append('  |   |    | |   |')
lines.append('  |   |    | |   |')
lines.append('----- |    | |   |')

'''loop for printing colored name'''
for t in lines:
    color_txt(t, random.choice(colors)) #random.choice - choose random element from list
