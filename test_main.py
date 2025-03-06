import unittest
from main import process_string, process_number, process_two_numbers_comma_delimited, process_two_numbers_newline_delimited, process_three_numbers, ThrowExceptionForNegativeNumbers, process_numbers_with_custom_delimiters

class TestProcessString(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        # Given
        input_string = ""
        expected = 0
        # When
        result = process_string(input_string)
        # Then
        self.assertEqual(result, expected)

class TestProcessNumber(unittest.TestCase):
    def test_number(self):
        # Given
        input_number = 1
        expected = 1
        # When
        result = process_number(input_number)
        # Then
        self.assertEqual(result, expected)

    def test_negative_number(self):
        # Given
        input_number = -1
        expected = -1
        # When
        result = process_number(input_number)
        # Then
        self.assertEqual(result, expected)

    def test_zero(self):
        # Given
        input_number = 0
        expected = 0
        # When
        result = process_number(input_number)
        # Then
        self.assertEqual(result, expected)

class TestProcessTwoNumbersCommaDelimited(unittest.TestCase):
    def test_two_numbers(self):
        # Given
        input_number1 = 1
        input_number2 = 2
        expected = 3
        # When
        result = process_two_numbers_comma_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        # Given
        input_number1 = -1
        input_number2 = -2
        expected = -3
        # When
        result = process_two_numbers_comma_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

    def test_zero(self):
        # Given
        input_number1 = 0
        input_number2 = 0
        expected = 0
        # When
        result = process_two_numbers_comma_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

class TestProcessTwoNumbersNewlineDelimited(unittest.TestCase):
    def test_two_numbers(self):
        # Given
        input_number1 = 1
        input_number2 = 2
        expected = 3
        # When
        result = process_two_numbers_newline_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        # Given
        input_number1 = -1
        input_number2 = -2
        expected = -3
        # When
        result = process_two_numbers_newline_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

    def test_zero(self):
        # Given
        input_number1 = 0
        input_number2 = 0
        expected = 0
        # When
        result = process_two_numbers_newline_delimited(input_number1, input_number2)
        # Then
        self.assertEqual(result, expected)

class TestProcessThreeNumbers(unittest.TestCase):
    def test_comma_delimited_numbers(self):
        # Given
        input_string = "1,2,3"
        expected = 6
        # When
        result = process_three_numbers(input_string)
        # Then
        self.assertEqual(result, expected)

    def test_newline_delimited_numbers(self):
        # Given
        input_string = "1\n2\n3"
        expected = 6
        # When
        result = process_three_numbers(input_string)
        # Then
        self.assertEqual(result, expected)

    def test_mixed_delimited_numbers(self):
        # Given
        input_string = "1\n2,3"
        expected = 6
        # When
        result = process_three_numbers(input_string.replace("\n", ","))
        # Then
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        # Given
        input_string = "1"
        
        # When
        result = process_three_numbers(input_string)
        # Then
        self.assertEqual(result, None)

    def test_no_input(self):
        # Given
        input_string = ""
        expected = None
        # When
        result = process_three_numbers(input_string)
        # Then
        self.assertEqual(result, expected)

class TestThrowExceptionForNegativeNumbers(unittest.TestCase):
    def test_negative_number(self):
        # Given
        input_number = -1
        # When
        # Then
        with self.assertRaises(ValueError):
            ThrowExceptionForNegativeNumbers(input_number)

    def test_positive_number(self):
        # Given
        input_number = 1
        # When
        # Then
        result = ThrowExceptionForNegativeNumbers(input_number)
        self.assertEqual(result, input_number)

    def test_zero(self):
        # Given
        input_number = 0
        # When
        # Then
        result = ThrowExceptionForNegativeNumbers(input_number)
        self.assertEqual(result, input_number)

class TestProcessNumbersWithCustomDelimiters(unittest.TestCase):
    def test_process_numbers_with_custom_delimiters(self):
        # Given
        input_string = "//;\n1;2"
        expected = 3
        # When
        result = process_numbers_with_custom_delimiters(input_string)
        # Then
        self.assertEqual(result, expected)

    def test_process_numbers_with_custom_delimiters2(self):
        # Given
        input_string = "//;\n1;2;3"
        expected = 6
        # When
        result = process_numbers_with_custom_delimiters(input_string)
        # Then
        self.assertEqual(result, expected)

    def test_process_numbers_with_custom_delimiters3(self):
        # Given
        input_string = "//;\n1;2;3;4"
        expected = 10
        # When
        result = process_numbers_with_custom_delimiters(input_string)
        # Then
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestProcessString('test_empty_string_returns_zero'))
    suite.addTest(TestProcessNumber('test_number'))
    suite.addTest(TestProcessNumber('test_negative_number'))
    suite.addTest(TestProcessNumber('test_zero'))
    suite.addTest(TestProcessTwoNumbersCommaDelimited('test_two_numbers'))
    suite.addTest(TestProcessTwoNumbersCommaDelimited('test_negative_numbers'))
    suite.addTest(TestProcessTwoNumbersCommaDelimited('test_zero'))
    suite.addTest(TestProcessTwoNumbersNewlineDelimited('test_two_numbers'))
    suite.addTest(TestProcessTwoNumbersNewlineDelimited('test_negative_numbers'))
    suite.addTest(TestProcessTwoNumbersNewlineDelimited('test_zero'))
    suite.addTest(TestProcessThreeNumbers('test_comma_delimited_numbers'))
    suite.addTest(TestProcessThreeNumbers('test_newline_delimited_numbers'))
    suite.addTest(TestProcessThreeNumbers('test_mixed_delimited_numbers'))
    suite.addTest(TestProcessThreeNumbers('test_no_delimiter'))
    suite.addTest(TestProcessThreeNumbers('test_no_input'))
    suite.addTest(TestThrowExceptionForNegativeNumbers('test_negative_number'))
    suite.addTest(TestThrowExceptionForNegativeNumbers('test_positive_number'))
    suite.addTest(TestThrowExceptionForNegativeNumbers('test_zero'))
    suite.addTest(TestProcessNumbersWithCustomDelimiters('test_process_numbers_with_custom_delimiters'))
    suite.addTest(TestProcessNumbersWithCustomDelimiters('test_process_numbers_with_custom_delimiters2'))
    suite.addTest(TestProcessNumbersWithCustomDelimiters('test_process_numbers_with_custom_delimiters3'))

    runner = unittest.TextTestRunner()
    runner.run(suite)