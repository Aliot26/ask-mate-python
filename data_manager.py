import database_connection as db_connect
from psycopg2.extensions import AsIs


@db_connect.connection_handler
def get_all_questions(cursor):
    cursor.execute("""
            SELECT id, submission_time, title, message
            FROM question
            ORDER BY submission_time DESC;
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


@db_connect.connection_handler
def sort_questions(cursor, conditions):
    cursor.execute("""
                        SELECT id, submission_time, title, message
                        FROM question
                        ORDER BY %(col_name)s %(order)s; 
                                   """,
                   {'col_name': AsIs(conditions['attribute']), 'order':AsIs(conditions['order'])})
    answers = cursor.fetchall()
    return answers

# def get_next_id(list_of_dict):
#     new_id = str(uuid.uuid4())[:6]
#     for dict in list_of_dict:
#         if dict['id'] == new_id:
#             get_next_id(list_of_dict)
#     return str(new_id)
