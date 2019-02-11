from flask import Flask, request
import re

app = Flask(__name__)


def get_comment_from_form():
    message = remove_parentheses(request.form.get('message'))
    message = check_is_not_empty(message)
    if message:
        comment = {
            'message': message
        }
        return comment
    else:
        return False


def check_conditions_of_sorting(conditions):
    attribute_list = ['submission_time', 'title']
    order_list = ['asc', 'desc']
    attribute = conditions['attribute']
    order = conditions['order']
    if attribute in attribute_list and order in order_list:
        return True
    else:
        return False


def remove_parentheses(string):
    string = re.sub('\<|\>|\{|\}|\[|\]', '', string)
    return string


def check_is_not_empty(string):
    if string == "":
        return False
    return string
