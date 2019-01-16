from flask import Flask, render_template, request, redirect, url_for

import data_manager
import connection

app = Flask(__name__)

@app.route('/list')
def route_list():
    all_questions = connection.get_all_data()

    return render_template('list.html', all_questions=all_questions)