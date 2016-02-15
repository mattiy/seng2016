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

    def test_V1_div3(self):	
	app = FizzBuzz()
		
	self.failIf(app.calc(3) != "Fizz")

    def test_V1_div5(self):
        app = FizzBuzz()

        self.failIf(app.calc(5) != "Buzz")

    def test_V1_div15(self):
        app = FizzBuzz()

        self.failIf(app.calc(15) != "FizzBuzz")

    def test_V1_number(self):
        app = FizzBuzz()

        self.failIf(app.calc(2) != 2)
		
def main():
    unittest.main()

if __name__ == "__main__":
    main()
