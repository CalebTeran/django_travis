from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions, exceptions
from library.users.serializers import RefreshTokenSerializer,UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView





class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise exceptions.AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect password!')

        response = Response()

        response.data = {
            'id': user.id,
            'email': user.email
        }
        return response

class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permissions_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = selft.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)