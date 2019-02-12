from flask import Blueprint
from flask_kit import Router, make_error

from .session import encode, decode


def create_api():
    blueprint = Blueprint('flask_session_api', __name__)
    router = Router(blueprint)

    @router.post('/decode', validate=decode_schema)
    def decode_view(data):
        """ Decode a flask session cookie """
        res = decode(data.get('data', ''))
        if not res:
            return make_error('error.failDecode')
        return res

    @router.post('/encode', validate=encode_schema)
    def encode_view(data):
        """ Encode a flask session cookie """
        res = encode(
            session_data=data.get('data'),
            secret=data.get('secret'),
            as_cookie=data.get('secret'),
            cookie_name=data.get('secret'),
            header=data.get('secret'),
            as_js=data.get('secret'),
        )
        if not res:
            return make_error('error.failEncode')
        return res

    return blueprint


decode_schema = {
    'session': {
        'type': 'string',
        'required': True,
    },
}

encode_schema = {
    'data': {
        'type': 'dict',
        'required': True,
    },
    'secret': {
        'type': 'string',
        'required': True,
    },
    'as_cookie': {
        'type': 'boolean',
        'default': False,
    },
    'as_header': {
        'type': 'boolean',
        'default': False,
    },
    'as_js': {
        'type': 'boolean',
        'default': False,
    },
}
