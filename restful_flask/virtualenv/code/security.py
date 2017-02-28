from werkzeug.security import safe_str_cmp      #USeful if using python2.7
from user import User

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

"""""
Prior to User class definition, we used this
#Dict inside List
users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

#Dict inside dict
username_mapping = { 'bob': {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}

#Dict inside dict
userid_mapping = { 1: {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
}
"""

def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)