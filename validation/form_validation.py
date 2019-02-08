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


def remove_parentheses(string):
    string = re.sub('\<|\>|\{|\}|\[|\]', '', string)
    return string


def check_is_not_empty(string):
    if string == "":
        return False
    return string
