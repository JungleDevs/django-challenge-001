from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from jungledevs.users.api.serializers import UserSerializer

User = get_user_model()


class BaseUserView(object):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class CreateUserView(BaseUserView, CreateAPIView):
    permission_classes = (AllowAny,)
