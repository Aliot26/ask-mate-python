import psycopg2
import data_manager as dm


def get_all_question():
    try:
        return dm.get_all_questions()
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def add_one_question(question):
    try:
        dm.add_one_question(question)
    except psycopg2.DatabaseError as e:
        print(e)
