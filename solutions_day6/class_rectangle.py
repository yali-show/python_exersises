class Rectangle:
    def __init__(self, lenght=0, weight=0):
        self.lenght = lenght
        self.weight = weight

    def calculate_area(self):
        area = self.lenght * self.weight

        return area

if __name__ == '__main__':
    message = input('Do you want add arguments?\nYes or No?: ')
    if message.lower() == 'yes':
        lenght = int(input('Lenght: '))
        weidth = int(input('Weidth: '))
        result = Rectangle(lenght, weidth).calculate_area()
        print(f'Your result: {result}')
    else:
        print(Rectangle().calculate_area())
