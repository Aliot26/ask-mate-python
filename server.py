from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)
