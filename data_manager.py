import uuid
import csv
import connection


def get_next_id(list_of_dict):
    new_id = str(uuid.uuid4())[:6]
    for dict in list_of_dict:
        if dict['id'] == new_id:
            get_next_id(list_of_dict)
    return str(new_id)


def get_one_question(question_id):
    with open(connection.QUESTION_FILE_PATH, newline='') as file:
        reader = csv.DictReader(file)
        for record in reader:
            if record['id'] == question_id:
                return record
