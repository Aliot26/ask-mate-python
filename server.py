from flask import Flask, render_template, request, redirect, url_for

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    all_questions = data_manager.get_all_questions()

    return render_template('list.html',
                           all_questions=all_questions,
                           )


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    question ={
        'title': request.form.get('title'),
        'message': request.form.get('message')
    }

    if request.method == 'POST':
        data_manager.add_one_question(question)
        return redirect('/')

    return render_template('edit.html',
                           form_url=url_for('route_add_question'),
                           page_title='Add Question',
                           button_title='Submit question',

                           )


@app.route('/question/<question_id>', methods=['GET'])
def route_question(question_id):
    question = data_manager.get_question(question_id)
    answers = data_manager.get_answers(question_id)

    return render_template('question.html',
                           question=question,
                           form_url=url_for('route_question', question_id=question_id),
                           page_title='Question',
                           answers=answers
                           )


@app.route('/question/new-answer/<question_id>', methods=['GET', 'POST'])
def route_add_answer(question_id):
    answer = {
        'question_id': question_id,
        'message': request.form.get('message')
    }
    question = data_manager.get_question(question_id)

    if request.method == 'POST':
        data_manager.add_one_answer(answer)
        return redirect('/')

    return render_template('answer.html',
                           page_title='Add Answer',
                           button_title='Submit answer',
                           answer=answer,
                           question_id=question_id,
                           question=question
                         )


@app.route('/list/sorted')
def route_list_sorted():
    all_data = data_manager.get_question()
    attribute = request.args.get('attribute')
    order = request.args.get('order')
    sorted_data = data_manager.sort_by_attributes(all_data, attribute, order)
    return render_template('list.html',
                           all_questions=sorted_data)


if __name__ == '__main__':
    app.secret_key = "some_key"
    app.run(
        host='0.0.0.0',
        port=7000,
        debug=True,
    )
