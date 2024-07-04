from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_token = request.headers.get('Authorization')
        if not auth_token:
            raise AuthenticationFailed('Invalid token type')

        user = User.get(authentication_token=auth_token)
        if user is None:
            raise AuthenticationFailed('Invalid token')
        return (user, None)
