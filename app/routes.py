from app import app
from flask import render_template, request, redirect, url_for, flash
import pandas as pd

from app.plots import *


@app.route('/',methods=['GET','POST'])
def index():
<<<<<<< HEAD
    df = pd.read_csv(r'app\data\tts_data.csv')
    fig = tts_figure(df)
=======
    df = pd.read_csv(r'app\data\tts_download.csv')
    fig = tts_histogram(df)
>>>>>>> 3050ca047880f7ec3549647ae21ce693ab7bbfde
    graphJSON = JSON_plot(fig)

    return render_template('index.html', graphJSON=graphJSON)
