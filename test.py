import unittest
import sys
from StringIO import StringIO

from app import FizzBuzz

class TestSuite(unittest.TestCase):

    def test_one(self):
        app = FizzBuzz()


        self.failIf(app.calc(1) != 1)

    def test_run(self):
        output = StringIO()

        app = FizzBuzz()
        app.run(100, output)

        self.failIf(len(output.getvalue().splitlines()) != 100)

    def test_V2_primes(self):
        app = FizzBuzz()

        self.failIf(app.calc(7) !=  "7 is a prime")
        self.failIf(app.calc(11) !=  "11 is a prime")
        self.failIf(app.calc(19) !=  "19 is a prime")
        self.failIf(app.calc(23) !=  "23 is a prime")
        self.failIf(app.calc(31) !=  "31 is a prime")
		
def main():
    unittest.main()

if __name__ == "__main__":
    main()
