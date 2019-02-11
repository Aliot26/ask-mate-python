import data_manager as dm
from validation import form_validation as fm


def get_all_question():
    try:
        return dm.get_all_questions()
    except ValueError as e:
        print(e)


def add_one_question(question):
    title = fm.remove_parentheses(question['title'])
    title = fm.check_is_not_empty(title)
    message = fm.remove_parentheses(question['message'])
    message = fm.check_is_not_empty(message)
    if title and message:
        question = {
            'title': title,
            'message': message
        }
        dm.add_one_question(question)
        return True
    else:
        return False


def get_question(question_id):
    try:
        return dm.get_question(question_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def sorting_questions(conditions):
    try:
        return dm.sort_questions(conditions)
    except psycopg2.DatabaseError as e:
        print(e)
        return []
