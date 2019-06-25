from unittest import TestCase
import homework2


class TestPrime(TestCase):

    def test_word(self):
        self.assertEqual(homework2.word(3), 'Fizz')

        self.assertEqual(homework2.word(5), 'Buzz')
        self.assertEqual(homework2.word(15), 'FizzBuzz')
        self.assertEqual(homework2.word(7), 7)

    def test_gcd(self):
        self.assertEqual(homework2.gcd(3, 678), 3)
        self.assertEqual(homework2.gcd(105, 5), 5)

    def test_restr(self):
        a = homework2.restr('3 5')
        self.assertTrue(type(a) is list)
