from flask import Flask, render_template, request, redirect, url_for
import data_manager
import connection

app = Flask(__name__)



@app.route('/')
@app.route('/list')
def route_list():
    all_questions = data_manager.sort_questions()

    return render_template('list.html',
                           all_questions=all_questions,
                           )


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    question = {
        'title':request.form.get('title'),
        'message':request.form.get('message')
    }

    if request.method == 'POST':


        data_manager.add_one_question(question)
        return redirect('/list')

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


@app.route('/question/<question_id>/new-answer', methods=['GET', 'POST'])
def route_add_answer(question_id):
    answer = {
        'question_id':question_id,
        'message':request.form.get('message')
    }
    question = data_manager.get_question(question_id)

    if request.method == 'POST':


        data_manager.add_one_answer(answer)
        return redirect('/list')

    return render_template('answer.html',
     #                      form_url=url_for('route_add_answer'),
                           page_title='Add Answer',
                           button_title='Submit answer',
                           answer=answer,
                           question_id=question_id,
                           question=question

                         )



@app.route('/list?order_by=title&order_direction=desc')
def route_sorted_list():
    try:
        user_stories = data_handler.get_all_user_story()
        attribute = request.args.get('attribute')
        order = request.args.get('order')
        user_stories = common.convert_number_to_integer(user_stories)
        sorted_stories = common.sort_by_attributes(user_stories, attribute, order)
        headers = ['ID', 'TITLE', 'USER STORY', 'ACCEPTANCE CRITERIA', 'BUSINESS VALUE', 'ESTIMATION', 'STATUS']
        return render_template('list.html',
                               user_stories=sorted_stories,
                               headers=headers)
    except UnboundLocalError:
        return route_list()

if __name__ == '__main__':
    app.secret_key = "some_key"
    app.run(
        host='0.0.0.0',
        port=7000,
        debug=True,
    )
