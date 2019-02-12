import json
from http import cookies as http_cookies

from flask import sessions, Flask
from flask.sessions import URLSafeTimedSerializer


def decode(secure_session):
    sec_cookie = sessions.SecureCookieSessionInterface()
    signer_kwargs = dict(
        key_derivation=sec_cookie.key_derivation,
        digest_method=sec_cookie.digest_method
    )
    ser = URLSafeTimedSerializer('irrelevant', salt=sec_cookie.salt,
                                 serializer=sec_cookie.serializer,
                                 signer_kwargs=signer_kwargs)
    decrypted = ser.loads_unsafe(secure_session, max_age=None)[1]
    return decrypted


class FakeApp(object):
    def __init__(self, secret):
        self.secret_key = secret


def make_session(secret, data):
    app = FakeApp(secret)
    sec_cookie = sessions.SecureCookieSessionInterface()
    return sec_cookie.get_signing_serializer(app).dumps(data)


def parse_json(data_or_filename, is_filename):
    if is_filename:
        try:
            with open(data_or_filename, 'r') as fp:
                data = fp.read()
        except OSError:
            return False, "Could not open '%s'" % data_or_filename
    else:
        data = data_or_filename

    try:
        return True, json.loads(data)
    except (ValueError, TypeError):
        return False, 'Invalid JSON'


def make_cookie(session, cookie_name=None, js=False, header=False):
    default_name = Flask.default_config.get('SESSION_COOKIE_NAME', 'session')
    name = cookie_name if cookie_name else default_name
    jar = http_cookies.SimpleCookie()
    jar[name] = session
    jar[name]['path'] = '/'
    jar[name]['expires'] = 'Session'
    if js:
        return jar[name].js_output().strip().replace('  ', '')
    if header:
        return jar[name]
    return str(jar[name]).replace('Set-Cookie:', '').strip()


def encode(secret=None, session_data=None, as_cookie=False,
           cookie_name=None, header=False, as_js=False):
    secure_session = make_session(secret, session_data)
    if as_cookie:
        output = make_cookie(secure_session, cookie_name, header=header)
    elif as_js:
        output = make_cookie(secure_session, cookie_name, js=as_js)
    else:
        output = secure_session

    return str(output).strip()