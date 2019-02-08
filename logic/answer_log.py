import psycopg2
import data_manager as dm


def get_answer(question_id):
    try:
        return dm.get_answers(question_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []
