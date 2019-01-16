from flask import Flask, render_template, request, redirect, url_for
import data_manager
import connection

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    all_questions = connection.get_all_data()

    return render_template('list.html',
                           all_questions=all_questions)


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        question = {
            'title': request.form.get('title'),
            'message': request.form.get('message'),
            'image': request.form.get('image')
        }

        data_manager.add_question(question)
        return redirect('/')

    return render_template('edit.html',
                           form_url=url_for('route_add_question'),
                           page_title='Add Question',
                           button='Add'
                           )


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_question(question_id: int):
    if request.method == 'POST':
        if request.form.get('id') != question_id:
            raise ValueError('The ID is not valid')

        answer = {
            'id': request.form.get('id'),
            'question_id': question_id,
            'message': request.form.get('message')
        }

        data_manager.add_answer(answer)
        return redirect('/')

    question = data_manager.get_one_question(question_id)
    answer = data_manager.get_one_answer(question_id)

    return render_template('list.html',
                           question=question,
                           answer=answer,
                           form_url=url_for('route_question', question_id=question_id),
                           page_title='Question'
                           )


@app.route('/question/<question_id>/new-answer')
def route_new_answer():
    pass


if __name__ == '__main__':
    app.secret_key = "P~#X\xfe\x00\xb4\xcb\x892\x00\xb2\xa6\x99\xb8\x87\xba3\xba\xa5\x826y\x8d\xa9"
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )



    # all_questions = [{'id': 0, 'submission_time': 1493368154, 'view_number': 29, 'vote_number': 7,
    #                   'title': 'How to make lists in Python?', 'message': 'I am totally new to this, any hints?',
    #                   'image': ''},
    #                  {'id': 1, 'submission_time': 1493068124, 'view_number': 15, 'vote_number': 9,
    #                   'title': "Wordpress loading multiple jQuery Versions",
    #                   'message': "I developed a plugin that uses the jquery booklet plugin this plu.", 'image': ''}]
