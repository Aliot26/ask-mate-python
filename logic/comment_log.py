import psycopg2
import data_manager as dm


def get_all_comments_by_question(question_id):
    try:
        return dm.get_all_comments_by_question(question_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def add_comment(comment):
    try:
        dm.add_one_comment(comment)
    except psycopg2.DatabaseError as e:
        print(e)