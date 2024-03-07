from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from users.models import User

class RegisterView(APIView):
    def post(self, request):
        print('registrando usuario...')
        return Response(status=status.HTTP_400_BAD_REQUEST)