import psycopg2
import data_manager as dm


def get_answers(question_id):
    try:
        return dm.get_answers(question_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def add_answer(answer):
    try:
        dm.add_one_answer(answer)
    except psycopg2.DatabaseError as e:
        print(e)


def get_one_answer(answer_id):
    try:
        return dm.get_one_answer(answer_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def update_answer(answer):
    try:
        dm.update_answer(answer)
    except psycopg2.DatabaseError as e:
        print(e)
