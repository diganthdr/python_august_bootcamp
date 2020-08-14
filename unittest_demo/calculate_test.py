import calculator

import unittest

class TestSimpleCalc(unittest.TestCase):

    def test_simple_add_integers(self):
        money = calculator.simple_add(34000, 23000)
        self.assertEqual(money, 57000)

    def test_simple_add_int_negative(self):
        money = calculator.simple_add(-3488, 23000)
        print("My account value: ", money)
        self.assertEqual(money, 19512)

    def test_simple_add_integer_text(self):
        money = calculator.simple_add( "four hundred", "three hundred")
        print("My account value: ", money)
        #self.assertEqual('foo'.upper(), 'FOO')

    def test_simple_add_integer_and_text(self):
        money = calculator.simple_add( "four hundred", "23000")
        print("My account value: ", money)
        #self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()


