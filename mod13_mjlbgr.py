import unittest
from datetime import datetime


def validate_symbol(symbol):
    return symbol.isalpha() and symbol.isupper() and 1 <= len(symbol) <= 7

def validate_chart_type(chart_type):
    return chart_type.isdigit() and int(chart_type) in [1, 2]

def validate_time_series(time_series):
    return time_series.isdigit() and int(time_series) in range(1, 5)

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestProject3Inputs(unittest.TestCase):

    def test_validate_symbol(self):
        self.assertTrue(validate_symbol('AAPL'))
        self.assertTrue(validate_symbol('GOOG'))
        self.assertFalse(validate_symbol('apple'))  
        self.assertFalse(validate_symbol('GOOGLE123')) 
        self.assertFalse(validate_symbol('LONGSYMBOLNAME'))

    def test_validate_chart_type(self):
        self.assertTrue(validate_chart_type('1'))
        self.assertTrue(validate_chart_type('2'))
        self.assertFalse(validate_chart_type('3'))
        self.assertFalse(validate_chart_type('a')) 

    def test_validate_time_series(self):
        self.assertTrue(validate_time_series('1'))
        self.assertTrue(validate_time_series('4'))
        self.assertFalse(validate_time_series('5'))  
        self.assertFalse(validate_time_series('0')) 

    def test_validate_start_date(self):
        self.assertTrue(validate_date('2022-01-01'))
        self.assertFalse(validate_date('01-01-2022')) 
        self.assertFalse(validate_date('2022/01/01')) 
        self.assertFalse(validate_date('2022-13-01'))  
    def test_validate_end_date(self):
        self.assertTrue(validate_date('2023-12-31'))
        self.assertFalse(validate_date('12-31-2023'))
        self.assertFalse(validate_date('2023-02-30')) 

if __name__ == '__main__':
    unittest.main()
