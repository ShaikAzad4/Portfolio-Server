from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

import os
import resend

from rest_framework.views import APIView
from rest_framework.response import Response

resend.api_key = os.environ.get("RESEND_API_KEY")

class Send_mail_api(APIView):

    def post(self, request):

        name = request.data.get("name")
        client_mail = request.data.get("mail")
        description = request.data.get("desc")

        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": ["shaikazad3131@gmail.com"],
            "subject": f"Portfolio Contact From {name}",
            "html": f"""
            <h3>Portfolio Contact</h3>
            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {client_mail}</p>
            <p><b>Message:</b> {description}</p>
            """
        })

        return Response({
            "message": "Mail sent successfully"
        })