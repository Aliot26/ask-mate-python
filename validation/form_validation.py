from flask import Flask, request
import re

app = Flask(__name__)


def get_question_from_form():
    title = remove_parentheses(request.form.get('title'))
    title = check_is_not_empty(title)
    message = remove_parentheses(request.form.get('message'))
    message = check_is_not_empty(message)
    if title and message:
        question = {
            'title': title,
            'message': message
        }
        return question
    else:
        return False


def get_answer_from_form():
    message = remove_parentheses(request.form.get('message'))
    message = check_is_not_empty(message)
    if message:
        answer = {
            'message': message
        }
        return answer
    else:
        return False


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


def check_conditions_of_sorting():
    attribute_list = ['submission_time', 'title']
    order_list = ['asc', 'desc']
    attribute = remove_parentheses(request.args.get('attribute'))
    attribute = check_is_not_empty(attribute)
    order = remove_parentheses(request.args.get('order'))
    order = check_is_not_empty(order)
    if attribute in attribute_list and order in order_list:
        conditions = {
            'attribute': attribute,
            'order': order
        }
        return conditions
    else:
        return False


def remove_parentheses(string):
    string = re.sub('\<|\>|\{|\}|\[|\]', '', string)
    return string


def check_is_not_empty(string):
    if string == "":
        return False
    return string
