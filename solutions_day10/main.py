import random


class Door:
    def __init__(self):
        self.opened = False
        self.prize = False
        self.picked = False

    def __str__(self):
        string = f"Opened={self.opened}, " \
                 f"Prize={self.prize}, " \
                 f"Picked={self.picked}"

        return string


class Guest:
    def pick_doors(self, doors):
        random_door = random.choice(doors)
        random_door.picked = True 

    def stay(self, doors):
        for door in doors:
            if door.picked == True:
                door.opened = True

    def change_door(self, doors):
        initial_door = None
        for door in doors:
            if door.picked:
                initial_door = door
        doors.remove(initial_door)
        initial_door.picked = False
        for door in doors:
            if door.opened == False:
                door.picked = True
                door.opened = True
        doors.append(initial_door)


class Monty:
    def open_non_prize(self, doors):
        for door in doors:
            if door.prize == False and door.picked == False:
                door.opened = True

    def get_results(self, doors):
        for door in doors:
            if door.opened == True and door.prize == True:
                return 1
        return 0


def generate_doors(number_of_doors):
    doors = []
    for i in range(number_of_doors):
        doors.append(Door())
    random_door = random.choice(doors)
    random_door.prize = True
    return doors


if __name__ == '__main__':
    guest = Guest()
    monty = Monty()
    win_counter = 0

    for i in range(1000):
        doors = generate_doors(3)
        guest.pick_doors(doors)
        monty.open_non_prize(doors)
        guest.change_door(doors)

        results = monty.get_results(doors)
        if results == 1:
            win_counter += 1

    print(win_counter)
