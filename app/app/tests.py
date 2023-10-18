"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Add numbers together and return result"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_sub_numbers(self):
        """Substract second number from first number and return result"""
        res = calc.sub(10, 4)

        self.assertEqual(res, 6)
