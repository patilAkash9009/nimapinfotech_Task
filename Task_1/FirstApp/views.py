from django.shortcuts import render
from .models import Client,Project
from .serializer import ClientSerializer,ProjectSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import AuthorOrReadOnly,AuthorAdminOrReadOnly

# list of all client
class Client_info(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# create new client
class CreateClient(generics.CreateAPIView):
    permission_classes = [AuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by =self.request.user)

# client info along with projects  # update info of client
class ClientAndProject(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# delete client from DataBases

class DeleteClient(generics.DestroyAPIView):





