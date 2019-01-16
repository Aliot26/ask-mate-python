import csv
import os

QUESTION_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/question.csv'
ANSWER_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'sample_data/answer.csv'
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']


def get_all_data(filename = QUESTION_FILE_PATH):
    with open(filename) as file:
        reader = csv.DictReader(file)
        all_data = [record for record in reader]
        return all_data


def save_data_in_csvfile(filename=QUESTION_FILE_PATH, data, headers):
    with open(filename, 'w', newline='')as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for record in data:
            writer.writerow(record)




