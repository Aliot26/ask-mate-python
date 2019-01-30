import uuid

import connection
import util
import database_connection as db_connect


@db_connect.connection_handler
def get_all_questions(cursor):
    cursor.execute("""
            SELECT id, submission_time, title, message
            FROM question;
                       """)
    all_question = cursor.fetchall()
    return all_question


@db_connect.connection_handler
def add_one_question(cursor, question):
    cursor.execute("""
                INSERT INTO question (submission_time, title, message)
                VALUES (NOW()::timestamp(0) , %(title)s, %(message)s)
                ON CONFLICT(id) DO NOTHING
                RETURNING id ;
                           """,
                   {'title': question['title'],
                    'message': question['message']
                    })


@db_connect.connection_handler
def add_one_answer(cursor, answer):
    cursor.execute("""
                    INSERT INTO answer (submission_time, question_id, message)
                    VALUES (NOW()::timestamp(0) , %(question_id)s, %(message)s)
                    ON CONFLICT(id) DO NOTHING;
                               """,
                   {'question_id': answer['question_id'],
                    'message': answer['message']
                    })


@db_connect.connection_handler
def get_question(cursor, question_id):
    cursor.execute("""
                SELECT id, submission_time, title, message
                FROM question
                WHERE id = %(question_id)s ;
                           """,
                   {'question_id': question_id})
    question = cursor.fetchone()
    return question


@db_connect.connection_handler
def get_answers(cursor, question_id):
    cursor.execute("""
                    SELECT id, submission_time, question_id, message
                    FROM answer
                    WHERE question_id = %(question_id)s ;
                               """,
                   {'question_id': question_id})
    answers = cursor.fetchall()
    return answers


def get_next_id(list_of_dict):
    new_id = str(uuid.uuid4())[:6]
    for dict in list_of_dict:
        if dict['id'] == new_id:
            get_next_id(list_of_dict)
    return str(new_id)


def sort_questions():
    all_questions = get_processed_data(connection.QUESTION_FILE_PATH)
    sorted_all_questions = sorted(all_questions, key=lambda q: q["submission_time"], reverse=True)
    return sorted_all_questions


def get_processed_data(filename):
    data = connection.get_all_data(filename)
    for record in data:
        date = record['submission_time']
        record['submission_time'] = util.convert_timestamp(date)
    return data


def sort_by_attributes(all_data, attribute, order):
    sort_order = None
    if order == 'desc':
        sort_order = True
    elif order == 'asc':
        sort_order = False
    sort_all_data = sorted(all_data, key=lambda k: k[attribute], reverse=sort_order)
    return sort_all_data
