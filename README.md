This is a tiny tool, service and chrome extension to decode, encode and brute-force flask sessions.

:warning: *This was created with the sole purpose of testing the security of my own applications, 
and should obviously not be used to attack or cause any type of damage to applications that you
do not own or haven't obtained the permission to do so. You are the sole responsible for the
consequences of using this.*

## Installing

To install this either use pip:
```bash
pip3 install git+https://github.com/rgcalsaverini/flask-session.git@0.1
```

or clone it and run setup:
```bash
git clone https://github.com/rgcalsaverini/flask-session
cd flask-session
python3 setup.py install

```

Just be sure that you are using python 3, this should not work on python 2.

## Usage

You can use it [live on the web UI](https://rui.calsaverini.com/en/flask-session-security).


After installing, just use `flask-session` form the command-line.

You can see the usage help by typing `flask-session --help`

### Examples

- Decoding a session cookie:

```bash
flask-session decode eyJ1c2VyIjoiNDQ1YTE2ODA0Mjk5NDRkNzg5NzAyMGI0NzZjNjdjZDkifQ.XFgrqA.3so8rQC8b37_FA50KS4pqfgNfL8

```

- Encoding a session cookie
```bash
flask-session encode mykey '{"secret": true}'
```

- Getting encode output as a header
```bash
flask-session --cookie --header encode mykey '{"userid": "john"}'

# You could inline it with curl, for example:
curl -i www.example.com \
    --header $(flask-session --cookie --header encode mykey '{"userid": "john"}')
```

- Getting encode output as a javascript snippet
```bash
flask-session --js encode mykey '{"role": "admin"}'
```


## Service

This is also [provided as a service here](https://flask-session.rui.calsaverini.com) trough a
REST API.
