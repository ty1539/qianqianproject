import jwt
from qianqianproject.settings import JWT_PRIVATE_KEY
from rest_framework_jwt.serializers import api_settings
from django.utils.encoding import smart_text
from django.utils.translation import ugettext as _
from rest_framework import exceptions
from rest_framework.authentication import (
    BaseAuthentication, get_authorization_header
)
from users.models import User


class WXJSONWebTokenAuthentication(BaseAuthentication):
    """
    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string specified in the setting
    `JWT_AUTH_HEADER_PREFIX`. For example:

        Authorization: JWT eyJhbGciOiAiSFMyNTYiLCAidHlwIj
    """
    www_authenticate_realm = 'api'

    def get_jwt_value(self, request):
        auth = get_authorization_header(request).split()
        auth_header_prefix = api_settings.JWT_AUTH_HEADER_PREFIX.lower()
        # print("type(auth)",type(auth),auth)
        if not auth:
            if api_settings.JWT_AUTH_COOKIE:
                return request.COOKIES.get(api_settings.JWT_AUTH_COOKIE)
            return None

        if smart_text(auth[0].lower()) != auth_header_prefix:
            return None
        # print('****************header****************')
        # print('auth',auth)
        if auth == [b'JWT']:
            return None
        if len(auth) == 1:
            msg = _('Invalid Authorization header. No credentials provided.')
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid Authorization header. Credentials string '
                    'should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        return auth[1]

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        return '{0} realm="{1}"'.format(api_settings.JWT_AUTH_HEADER_PREFIX, self.www_authenticate_realm)

    def authenticate(self, request):
        """
        Returns a two-tuple of `User` and token if a valid signature has been
        supplied using JWT-based authentication.  Otherwise returns `None`.
        """
        jwt_value = self.get_jwt_value(request)
        # print('jwt_value',jwt_value)
        if jwt_value is None:
            return None

        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            # print('Signature has expired')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            # print('Signature has expired')
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()

        user = self.authenticate_credentials(payload)

        return (user, jwt_value)

    def authenticate_credentials(self, payload):
        """
        Returns an active user that matches the payload's user id and email.
        """
        username = payload.get('username')

        if not username:
            msg = _('Invalid payload.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = User.objects.get(username=username)
        except Exception:
            msg = _('Invalid signature.')
            raise exceptions.AuthenticationFailed(msg)

        return user


def jwt_encode_handler(payload):
    return jwt.encode(
        payload,
        JWT_PRIVATE_KEY,
        api_settings.JWT_ALGORITHM
    ).decode('utf-8')


def jwt_decode_handler(token):
    payload = jwt.decode(token, JWT_PRIVATE_KEY, algorithms=[api_settings.JWT_ALGORITHM])
    return payload
