import data_manager as dm
from validation import form_validation as fv


def get_all_question():
    try:
        return dm.get_all_questions()
    except ValueError as e:
        print(e)
        return []


def add_one_question(question):
    title = fv.remove_parentheses(question['title'])
    title = fv.check_is_not_empty(title)
    message = fv.remove_parentheses(question['message'])
    message = fv.check_is_not_empty(message)
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
    except ValueError as e:
        print(e)
        return []


def sorting_questions(conditions):
    attribute = fv.remove_parentheses(conditions['attribute'])
    attribute = fv.check_is_not_empty(attribute)
    order = fv.remove_parentheses(conditions['order'])
    order = fv.check_is_not_empty(order)
    if fv.check_conditions_of_sorting(conditions):
        conditions = {
            'attribute': attribute,
            'order': order
        }
        sorted_data = dm.sort_questions(conditions)
        return sorted_data
    else:
        return []
