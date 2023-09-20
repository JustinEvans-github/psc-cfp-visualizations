import plotly.graph_objects as go
import statistics
import plotly
import numpy as np

# Convert Plotly figure to JSON
def JSON_plot(fig):

    # official method - https://www.geeksforgeeks.org/create-a-bar-chart-from-a-dataframe-with-plotly-and-flask/
    # data = [fig]
    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    # offline method - https://stackoverflow.com/questions/60803088/plotly-graph-empty-in-flask
    graphJSON = plotly.offline.plot(fig, 
                    config={"displayModeBar": False}, 
                    show_link=False, include_plotlyjs=False, 
                    output_type='div')

    return graphJSON

# Y-max of Plotly
# https://stackoverflow.com/questions/66583626/plotlyget-the-values-from-a-histogram-plotlyget-the-values-from-a-trace
def fig_y_max(fig):
    f = fig.full_figure_for_development(warn=False)

    xbins = f.data[0].xbins
    plotbins = list(np.arange(start=xbins['start'], stop=xbins['end']+xbins['size'], step=xbins['size']))
    counts, bins = np.histogram(list(f.data[0].x), bins=plotbins)
    
    return max(counts)

def tts_histogram(df):

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=df['Time to staff'], nbinsx=50, marker_color='#336b95',showlegend=False))

    # Selectable Dropdown
    # https://stackoverflow.com/questions/71622776/plotly-update-button-to-filter-dataset
    fig.update_layout(
        updatemenus=[
            {"buttons": [
                    {
                        "label": c,
                        "method": "update",
                        "args": [{"y": [df.loc[df['Period'] == c, 'Time to staff']]}],
                    }
                    for c in df["Period"].unique().tolist()
                ]
                
            }])

    # Custom Y-axis
    y_max = fig_y_max(fig)+1
    fig.update_layout(yaxis_range=[0,y_max])

    # y/x axis ticks and black lines
    fig.update_yaxes(showgrid=False,ticks="outside",tickson="boundaries",ticklen=5,showline=True, linecolor='black')
    fig.update_xaxes(showgrid=False,ticks="outside",tickson="boundaries",ticklen=5,showline=True, linecolor='black')


    # Median Line
    x_median = int(statistics.median(df['Time to staff']))
    fig.add_shape(
            go.layout.Shape(type='line', xref='x', yref='y',
            x0=x_median, y0=0, x1=x_median, y1=10, line={'dash': 'dash'}),)

    fig.update_layout(xaxis_title="Number of Days", yaxis_title="Number of cases") # titles
    fig.update_layout(bargap=0.01) # spacing

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)') # white background

    # Median Text
    x_middle = max(df['Time to staff'])/2
    text_median = f"--- Median ({x_median} days)"

    # fig.add_trace(go.Scatter(
    #     x=[x_middle],
    #     y=[y_max],
    #     mode="lines+text",
    #     name="Lines and Text",
    #     text=[text_median],
    #     textposition="bottom center",
    #     showlegend=False
    # ))

    fig.add_annotation(x=x_middle, y=y_max,
            text=text_median,
            showarrow=False,
            arrowhead=1)

    return fig
