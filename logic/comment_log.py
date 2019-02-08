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


def get_one_comment(comment_id):
    try:
        return dm.get_comment_by_id(comment_id)
    except psycopg2.DatabaseError as e:
        print(e)
        return []


def update_comment(comment):
    try:
        dm.update_comment(comment)
    except psycopg2.DatabaseError as e:
        print(e)
