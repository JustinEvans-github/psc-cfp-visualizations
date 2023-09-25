from app import app
from flask import render_template, request, redirect, url_for, flash
import pandas as pd

from app.plots import *

@app.route('/',methods=['GET','POST'])
def index():

    # data
    df = pd.read_csv(r'app\data\tts_data.csv')
    fig, metrics = tts_figure(df)
    graphJSON = JSON_plot(fig)

    # quicker graph for debugging
    # from plotly.subplots import make_subplots
    # fig = make_subplots(rows=2, cols=1,
    #                 vertical_spacing=0.15,
    #                 specs=[[{"type": "histogram"}],
    #                         [{"type": "table"}]])
    # graphJSON = JSON_plot(fig)

    return render_template('index.html',graphJSON=graphJSON, metrics=metrics)
