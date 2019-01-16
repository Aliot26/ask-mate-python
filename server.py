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
            'message': request.form.get('message')
        }

        data_manager.add_one_question(question)
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

        data_manager.add_one_answer(answer)
        return redirect('/')

    question = data_manager.get_one_question(question_id)
    answers = data_manager.get_answers(question_id)

    return render_template('list.html',
                           question=question,
                           answers=answers,
                           form_url=url_for('route_question', question_id=question_id),
                           page_title='Question'
                           )


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_add_answer(question_id: int):
    if request.method == 'POST':
        if request.form.get('id') != question_id:
            raise ValueError('The ID is not valid')

        answer = {
            'question_id': question_id,
            'message': request.form.get('message')
        }

        data_manager.add_one_answer(answer)
        return redirect('/')

    question = data_manager.get_one_question(question_id)

    return render_template('edit.html',
                           form_url=url_for('route_add_answer'),
                           question=question,
                           page_title='Add Answer',
                           button='Add'
                           )


if __name__ == '__main__':
    app.secret_key = "P~#X\xfe\x00\xb4\xcb\x892\x00\xb2\xa6\x99\xb8\x87\xba3\xba\xa5\x826y\x8d\xa9"
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
