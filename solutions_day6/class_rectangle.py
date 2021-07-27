class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width

        return area

if __name__ == '__main__':
    message = input('Do you want add arguments?\nYes or No?: ')
    if message.lower() == 'yes':
        length = int(input('Length: '))
        width = int(input('Width: '))
        result = Rectangle(length, width).calculate_area()
        print(f'Your result: {result}')
    else:
        print(Rectangle().calculate_area())
