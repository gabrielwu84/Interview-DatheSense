from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes

# empty authentication and permission classes needed to override default set in 
# settings.py otherwise new users who do not have credentials cannot even register! 
@api_view(['POST',])
@authentication_classes([])
@permission_classes([])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        s = status.HTTP_100_CONTINUE
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user'
            token = Token.objects.get(user=account).key
            data['token'] = token
            s = status.HTTP_201_CREATED
        else:
            data = serializer.errors
            s = status.HTTP_400_BAD_REQUEST
        return Response(data, status=s)