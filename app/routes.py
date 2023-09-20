from app import app
from flask import render_template, request, redirect, url_for, flash
import pandas as pd

from app.plots import *


@app.route('/',methods=['GET','POST'])
def index():
    df = pd.read_csv(r'app\data\tts_download.csv')
    fig = tts_histogram(df)
    graphJSON = JSON_plot(fig)

    return render_template('index.html', graphJSON=graphJSON)
