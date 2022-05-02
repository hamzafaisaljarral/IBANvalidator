from django.urls import path

from .views import ValidateAPIView

app_name = "validator"

urlpatterns = [
    path("", ValidateAPIView.as_view(),name='iban_validator'),
]