from rest_framework import viewsets

from .serializers import *
from roomManager.models import Service

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()  # mn ayy table badi jibon
    serializer_class = ServicesSerializer  # shu badu yesta3mel la ye2ra
