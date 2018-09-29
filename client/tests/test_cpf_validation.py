from django.test import TestCase

from client.validation import *


class CpfValidationTest(TestCase):
    good_values = (
        '288.666.827-30',
        '597.923.110-25',
        '981.108.954-09',
        '174.687.414-76',
        '774.321.431-10',
    )

    good_only_numbers_values = (
        '28866682730',
        '59792311025',
        '98110895409',
        '17468741476',
        '77432143110',
    )

    bad_values = (
        '288.666.827-31',
        '597.923.110-26',
        '981.108.954-00',
        '174.687.414-77',
        '774.321.431-11',
    )

    bad_only_numbers_values = (
        '28866682731',
        '59792311026',
        '98110895400',
        '17468741477',
        '77432143111',
    )

    invalid_values = (
        '00000000000',
        '11111111111',
        '22222222222',
        '33333333333',
        '44444444444',
        '55555555555',
        '66666666666',
        '77777777777',
        '88888888888',
        '99999999999'
    )

    def test_good_values(self):
        for cpf in self.good_values:
            result = validate_cpf(cpf)
            self.assertEqual(result, re.sub("[-\.]", "", cpf))

    def test_good_values_only_numbers(self):
        for cpf in self.good_only_numbers_values:
            result = validate_cpf(cpf)
            self.assertEqual(result, cpf)

    def test_bad_values(self):
        for cpf in self.bad_values:
            try:
                validate_cpf(cpf)
            except ValidationError as result:
                self.assertTrue('Invalid CPF number.' in result.messages[0])

    def test_bad_values_only_numbers(self):
        for cpf in self.bad_only_numbers_values:
            try:
                validate_cpf(cpf)
            except ValidationError as result:
                self.assertTrue('Invalid CPF number.' in result.messages[0])

    def test_alpha_value(self):
        cpf = '111.ABC'
        try:
            validate_cpf(cpf)
        except ValidationError as result:
            self.assertTrue('This field requires only numbers.' in result.messages[0])

    def test_special_character_value(self):
        cpf = '!@#$%&*()-_=+[]|"?><;:'
        try:
            validate_cpf(cpf)
        except ValidationError as result:
            self.assertTrue('This field requires only numbers.' in result.messages[0])

    def test_long_string_value(self):
        cpf = '1234567890123456789012345678901234567890123456789012'
        try:
            validate_cpf(cpf)
        except ValidationError as result:
            self.assertTrue('This field requires exactly 11 digits.' in result.messages[0])

    def test_invalid_values(self):
        for cpf in self.invalid_values:
            try:
                validate_cpf(cpf)
            except ValidationError as result:
                self.assertTrue('Invalid CPF number.' in result.messages[0])

    def test_empty_value(self):
        cpf = ''
        self.assertEqual(validate_cpf(cpf), '')
