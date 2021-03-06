# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# IBAN length of different country code

IBAN_COUNTRY_CODE_LENGTH = {'AL': 28,  # Albania
                            'AD': 24,  # Andorra
                            'AE': 23,  # United Arab Emirates
                            'AT': 20,  # Austria
                            'AZ': 28,  # Azerbaijan
                            'BA': 20,  # Bosnia and Herzegovina
                            'BE': 16,  # Belgium
                            'BG': 22,  # Bulgaria
                            'BH': 22,  # Bahrain
                            'BR': 29,  # Brazil
                            'CH': 21,  # Switzerland
                            'CR': 21,  # Costa Rica
                            'CY': 28,  # Cyprus
                            'CZ': 24,  # Czech Republic
                            'DE': 22,  # Germany
                            'DK': 18,  # Denmark
                            'DO': 28,  # Dominican Republic
                            'EE': 20,  # Estonia
                            'ES': 24,  # Spain
                            'FI': 18,  # Finland
                            'FO': 18,  # Faroe Islands
                            'FR': 27,  # France + Central African Republic, French Guiana, French Polynesia, Guadeloupe,
                            #          Martinique, Réunion, Saint-Pierre and Miquelon, New Caledonia,
                            #          Wallis and Futuna
                            'GB': 22,  # United Kingdom + Guernsey, Isle of Man, Jersey
                            'GE': 22,  # Georgia
                            'GI': 23,  # Gibraltar
                            'GL': 18,  # Greenland
                            'GR': 27,  # Greece
                            'GT': 28,  # Guatemala
                            'HR': 21,  # Croatia
                            'HU': 28,  # Hungary
                            'IE': 22,  # Ireland
                            'IL': 23,  # Israel
                            'IS': 26,  # Iceland
                            'IT': 27,  # Italy
                            'JO': 30,  # Jordan
                            'KZ': 20,  # Kazakhstan
                            'KW': 30,  # Kuwait
                            'LB': 28,  # Lebanon
                            'LI': 21,  # Liechtenstein
                            'LT': 20,  # Lithuania
                            'LU': 20,  # Luxembourg
                            'LV': 21,  # Latvia
                            'MC': 27,  # Monaco
                            'MD': 24,  # Moldova
                            'ME': 22,  # Montenegro
                            'MK': 19,  # Macedonia
                            'MT': 31,  # Malta
                            'MR': 27,  # Mauritania
                            'MU': 30,  # Mauritius
                            'NL': 18,  # Netherlands
                            'NO': 15,  # Norway
                            'PS': 29,  # Palestine
                            'PK': 24,  # Pakistan
                            'PL': 28,  # Poland
                            'PT': 25,  # Portugal + Sao Tome and Principe
                            'QA': 29,  # Qatar
                            'RO': 24,  # Romania
                            'RS': 22,  # Serbia
                            'SA': 24,  # Saudi Arabia
                            'SE': 24,  # Sweden
                            'SI': 19,  # Slovenia
                            'SK': 24,  # Slovakia
                            'SM': 27,  # San Marino
                            'TN': 24,  # Tunisia
                            'TR': 26,  # Turkey
                            'VG': 24}  # British Virgin Islands


class IBANValidator(object):
    """ A validator for International Bank Account Numbers (IBAN - ISO 13616-1:2007). """

    def __init__(self, include_countries=None):
        self.validation_countries = IBAN_COUNTRY_CODE_LENGTH.copy()
        self.include_countries = include_countries

    def verifyIBAN(self, value):
        """
        Validates the IBAN value using the official IBAN validation algorithm.
        for a basic formula please refer to this link
        https://en.wikipedia.org/wiki/International_Bank_Account_Number#Validating_the_IBAN
        """
        if value is None:
            return value

        value = value.upper().replace(' ', '').replace('-', '')

        # 1. Check that the total IBAN length is correct as per the country. If not, the IBAN is invalid.
        country_code = value[:2]
        if country_code in self.validation_countries:

            if self.validation_countries[country_code] != len(value):
                msg_params = {'country_code': country_code, 'number': self.validation_countries[country_code]}
                return ValidationError(_('%(country_code)s IBANs must contain %(number)s characters.') % msg_params)

        else:

            return ValidationError(_('%s is not a valid country code for IBAN.') % country_code)
        if self.include_countries and country_code not in self.include_countries:
            return ValidationError(_('%s IBANs are not allowed in this field.') % country_code)

        # 2. Move the four initial characters to the end of the string.
        value = value[4:] + value[:4]

        # 3. Replace each letter in the string with two digits, thereby expanding the string, where
        #    A = 10, B = 11, ..., Z = 35.
        value_digits = ''
        for x in value:
            ord_value = ord(x)
            if 48 <= ord_value <= 57:  # 0 - 9
                value_digits += x
            elif 65 <= ord_value <= 90:  # A - Z
                value_digits += str(ord_value - 55)
            else:
                return ValidationError(_('%s is not a valid character for IBAN.') % x)

        # 4. Interpret the string as a decimal integer and compute the remainder of that number on division by 97.
        if int(value_digits) % 97 != 1:
            return ValidationError(_('Not a valid IBAN.'))
        return True
