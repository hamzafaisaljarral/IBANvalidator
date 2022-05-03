from django.template.defaultfilters import upper
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .validate import IBANValidator


class ValidateAPIView(APIView):

    def get(self, request, *args, **kwargs):
        country_code = request.GET.get('country_code')
        iban = request.GET.get('iban')
        iban_func = IBANValidator(include_countries=upper(country_code))
        result = iban_func.verifyIBAN(value=iban)
        if result is not True:
            return Response({"IBAN INVALID": result}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"IBAN Valid": "country_code = {}, IBAN={}".format(country_code, iban)}, status=status.HTTP_200_OK)
