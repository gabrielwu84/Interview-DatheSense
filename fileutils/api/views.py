from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

# from account.models import Account
from fileutils.models import Upload
from fileutils.api.serializer import ListSerializer, UploadSerializer

from sensitive_calc.tasks import calc_score

class ApiUploadsListView(ListAPIView):
    def get_queryset(self):
        username = self.request.user
        return Upload.objects.filter(owner=username).order_by('dtm')
    serializer_class = ListSerializer
    authentication_class = (TokenAuthentication)
    permission_class = (IsAuthenticated)
    pagination_class = PageNumberPagination

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def api_upload_files_view(request):
    if request.method == "POST":
        context = { # needed for CurrentUserDefault() in serializer.py
            "request": request,
        }
        serializer = UploadSerializer(data=request.data, context=context)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"]="upload successful"
            calc_score.delay(1)
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

