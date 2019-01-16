import uuid
import connection
import util


def get_next_id(list_of_dict):
    new_id = str(uuid.uuid4())[:6]
    for dict in list_of_dict:
        if dict['id'] == new_id:
            get_next_id(list_of_dict)
    return str(new_id)


def add_one_question(question):
    all_data = connection.get_all_data(connection.QUESTION_FILE_PATH)
    question['id'] = get_next_id(all_data)
    question['submission_time'] = util.generate_timestamp()
    connection.save_data_in_csvfile(connection.QUESTION_FILE_PATH, question, connection.QUESTION_HEADER)


def add_one_answer(answer):
    all_data = connection.get_all_data(connection.ANSWER_FILE_PATH)
    answer['id'] = get_next_id(all_data)
    answer['submission_time'] = util.generate_timestamp()
    connection.save_data_in_csvfile(connection.ANSWER_FILE_PATH, answer, connection.ANSWER_HEADER)


def get_question(question_id=None):
    all_questions = connection.get_all_data(connection.QUESTION_FILE_PATH)
    if question_id:
        for question in all_questions:
            if question['id'] == question_id:
                return question
    return all_questions


def get_answers(question_id):
    answers = connection.get_all_data(connection.ANSWER_FILE_PATH)
    answers_to_question = []
    for answer in answers:
        if answer['question_id'] == question_id:
            answers_to_question.append(answer)
    return answers_to_question
