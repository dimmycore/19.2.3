import pytest
from app.calculator import Calculator


class TestCalcTwo:
    def setup(self):
        self.calc = Calculator

    def test_division(self):
        assert self.calc.division(self, 2, 2) == 1

    def test_subtraction(self):
        assert self.calc.subtraction(self, 100, 20) == 80

    def test_adding(self):
        assert self.calc.adding(self, 24, 26) == 50
