from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

@method_decorator(csrf_exempt, name='dispatch')
class Send_mail_api(APIView):

    def post(self, request):

        name = request.data.get('name')
        client_mail = request.data.get('mail')
        description = request.data.get('desc')

        subject = f"Portfolio Contact From {name}"

        description += f"""

Sender Name: {name}
Sender Email: {client_mail}
"""

        send_mail(
            subject,
            description,
            'shaikazad2121@gmail.com',
            ['shaikazad3131@gmail.com'],
            fail_silently=False
        )

        return Response({
            "message": "Mail sent successfully"
        })