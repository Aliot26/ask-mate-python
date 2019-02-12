import data_manager as dm
from auth import password_manager as pm

def check_exist_user(user):
    username = user['username']
    user_exist = dm.get_one_user(username)
    if user_exist:
        return user_exist


def hash_password(password):
    hash_pass = pm.hash_password(password)
    return hash_pass


def add_new_user(user):
    password = user['password']
    hash_pass = hash_password(password)
    user_new = {
        'password': hash_pass
    }
    user.update(user_new)

