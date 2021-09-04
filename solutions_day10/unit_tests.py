from unittest import TestCase
from main import *

class TestMorty(TestCase):
    def test_generate_doors(self):
        result = type(generate_doors(3))
        expected = list
        self.assertEqual(result, expected)

    def test_get_results(self):
        result = type(Monty.get_results(Monty, generate_doors(3)))
        expected = int
        self.assertEqual(result, expected)

    def test_pick_doors(self):
        doors_list = generate_doors(3)
        Guest.pick_doors(Guest, doors_list)
        for doors in doors_list:
            if doors.picked == True:
                result = True

        expected = True
        self.assertEqual(result ,expected)

    def test_stay(self):
        doors_list = generate_doors(3)
        Guest.pick_doors(Guest, doors_list)
        Guest.stay(Guest, doors_list)
        for doors in doors_list:
            if doors.opened == True:
                result = True

        expected = True
        self.assertEqual(result, expected)