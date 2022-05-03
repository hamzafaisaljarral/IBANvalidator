from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class IBANValidatorAPIViewTestCase(APITestCase):

    def test_case_1(self):
        """
        Test to verify iban
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=PK&iban=PK36 SCBL 0000 0011 2345 6702")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_case_2(self):
        """
        Test to verify iban with wrong country code and iban
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=ABC&iban=123456")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_case_3(self):
        """
        Test to verify iban with wrong country code correct valid IBAN
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=AE&iban=SE45 5000 0000 0583 9825 7466")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_case_4(self):
        """
        Test to verify iban with correct country code wrong IBAN
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=SE&iban=PK45 5000 0000 0583 9825 7466")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_case_5(self):
        """
        Test to verify iban with lower case country code correct IBAN
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=se&iban=SE45 5000 0000 0583 9825 7466")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_case_6(self):
        """
        Test to verify iban with lower case country code lowercase correct IBAN
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=se&iban=se45 5000 0000 0583 9825 7466")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_case_7(self):
        """
        Test to verify iban with correct country code correct IBAN but not in our dict
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=VA&iban=VA59001123000012345678")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_case_8(self):
        """
        Test to verify iban with correct country code correct IBAN without spaces
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=SE&iban=SE4550000000058398257466")
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_case_9(self):
        """
        Test to verify iban with correct country code wrong IBAN with same length as mention
        """
        response = self.client.get(f"{reverse('validator:iban_validator')}?country_code=SE&iban=SE4550000000058398257900")
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)




