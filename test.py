import unittest
import task

class MyTestCase(unittest.TestCase):
    def test_prime_numbers_arguments_strings(self):
        self.assertEqual(0, len(task.prime_numbers('string1', 'string2')))

    def test_prime_numbers_low_greater_than_high(self):
        self.assertEqual(0, len(task.prime_numbers(6, 2)))

    def test_prime_numbers_float_range(self):
        self.assertEqual(4, len(task.prime_numbers(3.5, 15.6)))

    def test_prime_numbers_correct_input_empty_result(self):
        self.assertEqual(0, len(task.prime_numbers(3.5, 3.6)))

    def test_prime_numbers(self):
        self.assertEqual([3, 5, 7, 11, 13, 17, 19, 23], task.prime_numbers(2.5, 24))

    def test_text_stat_file_does_not_exist(self):
        self.assertEqual('File does not exist', task.text_stat('nonexistentfile.txt').get('error'))

    def test_text_stat_incorrect_filename(self):
        self.assertEqual('Incorrect argument type', task.text_stat(3.1416).get('error'))

    def test_text_stat_file_exists(self):
        self.assertIsNone(task.text_stat('file.txt').get('error'))

    def test_text_stat_paragraph_amount(self):
        self.assertEqual(4, task.text_stat('file.txt').get('paragraph_amount'))

    def test_text_stat_word_amount(self):
        self.assertEqual(158, task.text_stat('file.txt').get('word_amount'))

    def test_text_stat_bilingual_word_amount(self):
        self.assertEqual(0, task.text_stat('file.txt').get('bilingual_word_amount'))

    def test_text_stat_word_amount_testfile(self):
        self.assertEqual(5, task.text_stat('testfile.txt').get('word_amount'))

    def test_text_stat_bilingual_word_amount_testfile(self):
        self.assertEqual(3, task.text_stat('testfile.txt').get('bilingual_word_amount'))

    def test_text_stat_letter_amount_testfile(self):
        self.assertEqual((4, 2), task.text_stat('testfile.txt').get('a'))

    def test_roman_numerals_to_int_if_not_a_string(self):
        self.assertIsNone(task.roman_numerals_to_int(42))

    def test_roman_numerals_to_int_four_roman_numerals_in_a_row(self):
        self.assertIsNone(task.roman_numerals_to_int('XXXXVII'))

    def test_roman_numerals_to_int_incorrect_roman_form(self):
        self.assertIsNone(task.roman_numerals_to_int('XXVXVII'))

    def test_roman_numerals_to_int_with_addition(self):
        self.assertEqual(16, task.roman_numerals_to_int('XVI'))

    def test_roman_numerals_to_int_with_subtraction(self):
        self.assertEqual(24, task.roman_numerals_to_int('XXIV'))

    def test_roman_numerals_to_int_max_roman_numeral(self):
        self.assertEqual(3999, task.roman_numerals_to_int('MMMCMXCIX'))

    def test_roman_numerals_to_int_reverse_max_roman_numeral(self):
        self.assertIsNone(task.roman_numerals_to_int('XICXMCMMM'))


if __name__ == '__main__':
    unittest.main()
