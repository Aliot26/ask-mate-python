from flask import Flask, render_template, request, redirect, url_for

import data_manager
from logic import question_log as ql
from logic import answer_log as al
from logic import comment_log as cl
from validation import form_validation as fv

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    warning = ""
    all_questions = ql.get_all_question()
    if not all_questions:
        warning = "No data"
    return render_template('list.html',
                           all_questions=all_questions,
                           warning=warning
                           )


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    warning = ""
    if request.method == 'POST':
        question = fv.get_question_from_form()
        if question:
            ql.add_one_question(question)
            return redirect('/')
        else:
            warning = "Please, fill in form correctly"
    return render_template('edit.html',
                           form_url=url_for('route_add_question'),
                           page_title='Add Question',
                           button_title='Submit question',
                           warning=warning
                           )


@app.route('/question/<question_id>', methods=['GET'])
def route_question(question_id):
    question = ql.get_question(question_id)
    answers = al.get_answers(question_id)
    all_comments = cl.get_all_comments_by_question(question_id)
    return render_template('question.html',
                           question=question,
                           form_url=url_for('route_question', question_id=question_id),
                           page_title='Question',
                           answers=answers,
                           all_comments=all_comments
                           )


@app.route('/question/new-answer/<question_id>', methods=['GET', 'POST'])
def route_add_answer(question_id):
    warning = ""
    question = ql.get_question(question_id)
    if request.method == 'POST':
        answer = fv.get_answer_from_form()
        if answer:
            answer['question_id']= question_id
            al.add_answer(answer)
            return redirect('/question/{}'.format(question_id))
        else:
            warning = "Please, fill in form correctly"

    return render_template('answer.html',
                           page_title='Add Answer',
                           button_title='Submit answer',
                           form_url=url_for('route_add_answer', question_id=question_id),
                           question_id=question_id,
                           question=question,
                           warning=warning)


@app.route('/list/sorted')
def route_list_sorted():
    conditions = {
        'attribute': request.args.get('attribute'),
        'order': request.args.get('order')
    }
    sorted_data = data_manager.sort_questions(conditions)

    return render_template('list.html',
                           all_questions=sorted_data)


@app.route('/edit-answer/<id>', methods=['GET', 'POST'])
def route_edit_answer(id):
    warning = ""
    answer = al.get_one_answer(id)
    question_id = answer['question_id']
    question = ql.get_question(question_id)
    if request.method == "POST":
        answer = fv.get_answer_from_form()
        if answer:
            answer['id'] = id
            al.update_answer(answer)
            return redirect('/question/{}'.format(question_id))
        else:
            warning = "Please, fill in form correctly"
    return render_template('answer.html',
                           page_title='Add Answer',
                           button_title='Submit answer',
                           edit_answer=answer,
                           question=question,
                           warning=warning)


@app.route('/answer/new-comment/<answer_id>', methods=['GET', 'POST'])
def route_add_comment(answer_id):
    answer = data_manager.get_one_answer(answer_id)
    comment = {
        'answer_id': answer_id,
        'message': request.form.get('message'),
        'question_id': answer['question_id']
    }
    if request.method == 'POST':
        data_manager.add_one_comment(comment)
        return redirect('/question/{}'.format(comment['question_id']))

    return render_template('comment.html',
                           page_title='Add comment',
                           button_title='Submit Comment',
                           form_url=url_for('route_add_comment', answer_id=answer_id),
                           answer_id=answer_id,
                           answer=answer
                           )


@app.route('/edit-comment/<comment_id>', methods=['GET', 'POST'])
def route_edit_comment(comment_id):
    comment = data_manager.get_comment_by_id(comment_id)
    question_id = comment['question_id']
    if request.method == "POST":
        comment = {
            'id': comment['id'],
            'message': request.form.get('message')
        }
        data_manager.update_comment(comment)
        return redirect('/question/{}'.format(question_id))
    return render_template('comment.html',
                           page_title='Edit comment',
                           button_title='Submit comment',
                           edit_comment=comment
                           )


if __name__ == '__main__':
    app.secret_key = "some_key"
    app.run(
        host='0.0.0.0',
        port=7000,
        debug=True,
    )
