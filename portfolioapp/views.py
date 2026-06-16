
from rest_framework.response import Response
from rest_framework.views import APIView
import os
import resend

resend.api_key = os.environ.get("RESEND_API_KEY")

class Send_mail_api(APIView):

    def post(self, request):
        try:
            name = request.data.get("name")
            client_mail = request.data.get("mail")
            description = request.data.get("desc")

            result = resend.Emails.send({
                "from": "shaikazad2121@gmail.com",
                "to": ["shaikazad3131@gmail.com"],
                "subject": f"Portfolio Contact From {name}",
                "html": f"""
                <h3>Portfolio Contact</h3>
                <p>Name: {name}</p>
                <p>Email: {client_mail}</p>
                <p>Message: {description}</p>
                """
            })

            return Response({
                "message": "success",
                "result": str(result)
            })

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=500)