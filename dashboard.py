import pathlib
import os
import dash
#import dash_core_components as dcc
#import dash_html_components as html
from dash import dcc
from dash import html
import pandas as pd

app_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(os.path.join(app_path, os.path.join("data", "c_1.csv")))
df.columns = ['time', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y', 'gyro_z']

app = dash.Dash(__name__, url_base_pathname='/dashboard/')
server = app.server

theme = {
    'background': '#111111',
    'text': '#FFFFFF'
}


def build_banner():
    return html.Div(
        className='col-sm-10 row banner',
        children=[
            html.Div(
                className='banner-text',
                children=[
                    html.H5('Accelerometer data'),
                ],
            ),
        ],
    )


def build_graph():
    return dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': df['time'],
                    'y': df['acc_x'],
                    'name': 'acc_x',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['acc_y'],
                    'name': 'acc_y',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'][:-1],
                    'y': df['acc_z'][:-1],
                    'name': 'acc_z',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_x'],
                    'name': 'gyro_x',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_y'],
                    'name': 'gyro_y',
                    'marker': {'size': 12}
                },
                {
                    'x': df['time'],
                    'y': df['gyro_z'],
                    'name': 'gyro_z',
                    'marker': {'size': 12}
                },
            ],
            'layout': {
                'title': 'Gyroscope Data Visualization',
                'xaxis': {
                'title': 'Timestamp, ms',
                'font': {
                    'color': theme['text']
                }
                },
                'yaxis': {
                'title': 'Multiple gyroscope data',
                'font': {
                    'color': theme['text']
                }
                },
                'plot_bgcolor': theme['background'],
                'paper_bgcolor': theme['background'],
                'font': {
                    'color': theme['text']
                }
            }
        }
    )


app.layout = html.Div(
    className='big-app-container',
    children=[
        build_banner(),
        html.Div(
            className='app-container',
            children=[
                build_graph(),
            ]
        )
    ]
)
