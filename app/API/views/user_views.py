from rest_framework import generics
from app.Users.models import UserProfile
from app.API.serializers.user_serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

class NewUserListView(generics.ListAPIView):
    queryset = UserProfile.objects.filter(contacted="new")
    serializer_class = UserSerializer

class UpdateUserStatusView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.contacted = "old"
        user.save(update_fields=['contacted'])
        return Response({"message": "Статус обновлен"}, status=status.HTTP_200_OK)