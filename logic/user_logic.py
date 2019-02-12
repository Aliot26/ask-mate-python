import data_manager as dm
from auth import password_manager as pm


def check_exist_user(username):
    user_exist = dm.get_one_user(username)
    if user_exist:
        return user_exist


def hash_password(password):
    hash_pass = pm.hash_password(password)
    return hash_pass


def add_new_user(user):
    username = user['username']
    if not check_exist_user(username):
        dm.add_one_user(user)
        return True
    return False


def check_pass(login_user):
    username = login_user['username']
    pass_from_form = login_user['password']
    user_from_base = check_exist_user(username)
    pass_from_base = user_from_base['password']
    if user_from_base:
        verify = pm.verify_password(pass_from_form, pass_from_base)
    return verify
