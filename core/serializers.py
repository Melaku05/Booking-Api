from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']