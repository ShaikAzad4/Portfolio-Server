from django.urls import path
from portfolioapp.views import Send_mail_api

urlpatterns = [
    path('send-mail/',Send_mail_api.as_view(), name='send_mail')
]