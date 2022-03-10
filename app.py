from random import random
import dash
from dash import html
import pandas as pd
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import utils
from datetime import datetime
from dash_table import DataTable
import datetime


class myclass:
    def __init__(self):
        self.df = pd.DataFrame()
        self.dfprime = pd.DataFrame()
        self.list_press = []
        self.list_time = []
        self.list_p = []
        self.list_t = []
        self.list_pressprime = []
        self.list_timeprime = []
        self.list_pprime = []
        self.list_tprime = []

myclass = myclass()

card = html.Div(children = [
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Assis debout", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '1'),
                dbc.ListGroupItem("Etape 2", id = '2'),
                dbc.ListGroupItem("Etape 3", id = '3'),
                dbc.ListGroupItem("Etape 4", id = '4'),
                dbc.ListGroupItem("Etape 5", id = '5'),
            ],
            flush=True,
        ),
        style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
    ),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Assis debout[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '6'),
                dbc.ListGroupItem("Etape 2", id = '7'),
                dbc.ListGroupItem("Etape 3", id = '8'),
                dbc.ListGroupItem("Etape 4", id = '9'),
                dbc.ListGroupItem("Etape 5", id = '10'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche vers une cible", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '11'),
                dbc.ListGroupItem("Etape 2", id = '12'),
                dbc.ListGroupItem("Etape 3", id = '13'),
                dbc.ListGroupItem("Etape 4", id = '14'),
                dbc.ListGroupItem("Etape 5", id = '15'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche vers une cible[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '16'),
                dbc.ListGroupItem("Etape 2", id = '17'),
                dbc.ListGroupItem("Etape 3", id = '18'),
                dbc.ListGroupItem("Etape 4", id = '19'),
                dbc.ListGroupItem("Etape 5", id = '20'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche talon pointe", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '21'),
                dbc.ListGroupItem("Etape 2", id = '22'),
                dbc.ListGroupItem("Etape 3", id = '23'),
                dbc.ListGroupItem("Etape 4", id = '24'),
                dbc.ListGroupItem("Etape 5", id = '25'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche talon pointe[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '26'),
                dbc.ListGroupItem("Etape 2", id = '27'),
                dbc.ListGroupItem("Etape 3", id = '28'),
                dbc.ListGroupItem("Etape 4", id = '29'),
                dbc.ListGroupItem("Etape 5", id = '30'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
)
], id = "step_card", style = {'textAlign' : 'center'})

card2 = html.Div(children = [
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche panneaux vichy", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '1prime'),
                dbc.ListGroupItem("Etape 2", id = '2prime'),
                dbc.ListGroupItem("Etape 3", id = '3prime'),
                dbc.ListGroupItem("Etape 4", id = '4prime'),
                dbc.ListGroupItem("Etape 5", id = '5prime'),
            ],
            flush=True,
        ),
        style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
    ),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Marche panneaux vichy[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '6prime'),
                dbc.ListGroupItem("Etape 2", id = '7prime'),
                dbc.ListGroupItem("Etape 3", id = '8prime'),
                dbc.ListGroupItem("Etape 4", id = '9prime'),
                dbc.ListGroupItem("Etape 5", id = '10prime'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Ramassage cube", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '11prime'),
                dbc.ListGroupItem("Etape 2", id = '12prime'),
                dbc.ListGroupItem("Etape 3", id = '13prime'),
                dbc.ListGroupItem("Etape 4", id = '14prime'),
                dbc.ListGroupItem("Etape 5", id = '15prime'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Ramassage cube[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '16prime'),
                dbc.ListGroupItem("Etape 2", id = '17prime'),
                dbc.ListGroupItem("Etape 3", id = '18prime'),
                dbc.ListGroupItem("Etape 4", id = '19prime'),
                dbc.ListGroupItem("Etape 5", id = '20prime'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Dessin", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '21prime'),
                dbc.ListGroupItem("Etape 2", id = '22prime'),
                dbc.ListGroupItem("Etape 3", id = '23prime'),
                dbc.ListGroupItem("Etape 4", id = '24prime'),
                dbc.ListGroupItem("Etape 5", id = '25prime'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
),
    dbc.Card(
        dbc.ListGroup(
            [
                html.H5("Dessin[I]", className="mb-1"),
                dbc.ListGroupItem("Etape 1", id = '26prime'),
                dbc.ListGroupItem("Etape 2", id = '27prime'),
                dbc.ListGroupItem("Etape 3", id = '28prime'),
                dbc.ListGroupItem("Etape 4", id = '29prime'),
                dbc.ListGroupItem("Etape 5", id = '30prime'),
            ],
            flush=True,
        ),
    style={"width": "18rem", 'background-color' : 'CadetBlue', 'width': '16%', 'display': 'inline-block', 'textAlign' : 'center'},
)
], id = "step_cardprime", style = {'textAlign' : 'center'})

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = html.Div(
    children=[
        html.H1(children="Espace chronomètre", style = {'textAlign' : 'center'}),
        html.P(
            children='''Appuyez sur le buzzer pour débuter l'enregistrement. Une fois l'étape terminée, rappuyez sur le buzzer afin d'arrêter l'enregistrement. Veillez à terminer les 5 épreuves.\n
            Le bouton précédent n'est à utiliser qu'une fois l'étape en cours terminée.''',
        style = {'textAlign' : 'center', 'margin-left' : '2%', 'margin-right' : '2%'}),
        html.Div([html.P(id = "text_green"),
            html.Div(children = [
                dbc.Button('Buzzer', size="lg", color="primary", className="me-1", id = "green"), 
                dbc.Button('Précédent', size="md", color="warning", className="me-1", id = "precedent"), 
            ]),
        ],
        style={'textAlign': 'center'}),
        html.Div(children = card, id = "table", style = {'margin-top' : '10px'}),
        html.Div([html.P(id = "text_greenprime"),
        html.Div(children = [
            dbc.Button('Buzzer [I]', size="lg", color="primary", className="me-1", id = "greenprime"),
            dbc.Button('Précédent', size="md", color="warning", className="me-1", id = "precedentprime")
        ]),
        ],
        style={'textAlign': 'center'}),
        html.Div(children = card2, id = "tableprime", style = {'margin-top' : '10px'}),
        html.Div(dbc.Button('Résultats 1', id = "button", color="info", className="me-1")),
        html.Div(dbc.Button('Résultats 2', id = "buttonprime", color="info", className="me-1")),
        html.Div(dbc.Modal(
            [
                dbc.ModalHeader("Attention"),
                dbc.ModalBody("Veuillez terminer toutes les épreuves pour obtenir les résultats."),
            ],
            id="modal",
            is_open=False,
        )),
        html.Div(dbc.Modal(
            [
                dbc.ModalHeader("Attention [I]"),
                dbc.ModalBody("Veuillez terminer toutes les épreuves pour obtenir les résultats."),
            ],
            id="modalprime",
            is_open=False,
        )),
        html.Div(dbc.Button('Recommencer', id = "button_reset", color="warning", className="me-1")),
        html.Div(children = [DataTable(id = "result", data = [], export_format = 'xlsx')]),
        html.Div(DataTable(id = "resultprime", data = [], export_format = 'xlsx')),
        ]
        , style = {'background' : 'CadetBlue'})
        
@app.callback(
    Output(component_id='green', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 2 != 0:
        return {'height':'8%', 'width':'8%'}
    else:
        return {'height':'10%', 'width':'10%'}

@app.callback(
    Output(component_id='text_green', component_property='children'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 2 != 0:
        return ("Enregistrement en cours...")
    else:
        return ("Il n'y a pas d'enregistrement en cours.")

@app.callback(
    Output(component_id='1', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)


def update_output(n_clicks):
    if n_clicks != None and n_clicks != 0:
        list_p, list_t = utils.step_timer(n_clicks, myclass.list_press, myclass.list_time)
    if len(myclass.list_time) >= 2:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='2', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 4:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='3', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    # print("len listtime =", len(myclass.list_time))
    if len(myclass.list_time) >= 6:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='4', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 8:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='5', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 10:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='6', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 12:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='7', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 14:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='8', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 16:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='9', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 18:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='10', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 20:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='11', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 22:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='12', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 24:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='13', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 26:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='14', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 28:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='15', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 30:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='16', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 32:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='17', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 34:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='18', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 36:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='19', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 38:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='20', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 40:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='21', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 42:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='22', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 44:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='23', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 46:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='24', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 48:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='25', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 50:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='26', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 52:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='27', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 54:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='28', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 56:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='29', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 58:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='30', component_property='style'),
    Input(component_id='green', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_time) >= 60:
        return {'background-color' : 'green'}
        ##########################################################
@app.callback(
    Output(component_id='greenprime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 2 != 0:
        return {'height':'8%', 'width':'8%'}
    else:
        return {'height':'10%', 'width':'10%'}

@app.callback(
    Output(component_id='text_greenprime', component_property='children'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if n_clicks % 2 != 0:
        return ("Enregistrement en cours...")
    else:
        return ("Il n'y a pas d'enregistrement en cours.")

@app.callback(
    Output(component_id='1prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)


def update_output(n_clicks):
    if n_clicks != None and n_clicks != 0:
        list_pprime, list_tprime = utils.step_timer(n_clicks, myclass.list_pressprime, myclass.list_timeprime)
    if len(myclass.list_timeprime) >= 2:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='2prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 4:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='3prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 6:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='4prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 8:
        return {'background-color' : 'green'}

@app.callback(
    Output(component_id='5prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 10:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='6prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 12:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='7prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 14:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='8prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 16:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='9prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 18:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='10prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 20:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='11prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 22:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='12prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 24:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='13prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 26:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='14prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 28:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='15prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 30:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='16prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 32:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='17prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 34:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='18prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 36:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='19prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 38:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='20prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 40:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='21prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 42:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='22prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 44:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='23prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 46:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='24prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 48:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='25prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 50:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='26prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 52:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='27prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 54:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='28prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 56:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='29prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 58:
        return {'background-color' : 'green'}
@app.callback(
    Output(component_id='30prime', component_property='style'),
    Input(component_id='greenprime', component_property='n_clicks')
)

def update_output(n_clicks):
    if len(myclass.list_timeprime) >= 60:
        return {'background-color' : 'green'}
    
@app.callback(
    [Output("result", "data"), Output('result', 'columns')],
    Input(component_id='button', component_property='n_clicks')
)

def table(n_clicks):
    # print('table nclicks = ', n_clicks)
    if n_clicks != None and n_clicks != 0:
        i = 0
        j = 0
        list_delta = []  
        # print('list time = ', len(myclass.list_time))
        while j < 30:
            item1 = datetime.datetime.strptime(myclass.list_time[i], '%Y-%m-%d %H:%M:%S.%f')
            item2 = datetime.datetime.strptime(myclass.list_time[i+1], '%Y-%m-%d %H:%M:%S.%f')
            delta = (item2 - item1)
            list_delta.append(delta.total_seconds())
            j += 1
            i += 2
        # print('len delta = ',len(list_delta))
        list_index = [1, 2, 3, 4, 5]
        myclass.df.index = list_index
        myclass.df['Assis debout'] = list_delta[0:5]
        myclass.df['Assis debout[I]'] = list_delta[5:10]
        myclass.df['Marche vers une cible'] = list_delta[10:15]
        myclass.df['Marche vers une cible[I]'] = list_delta[15:20]
        myclass.df['Marche panneaux vichy'] = list_delta[20:25]
        myclass.df['Marche panneaux vichy[I]'] = list_delta[25:30]
        print(myclass.df)
        return (myclass.df.to_dict('records'), [{"name": i, "id": i} for i in myclass.df.columns])

@app.callback(
    [Output("resultprime", "data"), Output('resultprime', 'columns')],
    Input(component_id='buttonprime', component_property='n_clicks')
)

def table(n_clicks):
    # print('table nclicks = ', n_clicks)
    if n_clicks != None and n_clicks != 0:
        i = 0
        j = 0
        list_delta = []  
        # print('list time = ', len(myclass.list_time))
        while j < 30:
            item1 = datetime.datetime.strptime(myclass.list_timeprime[i], '%Y-%m-%d %H:%M:%S.%f')
            item2 = datetime.datetime.strptime(myclass.list_timeprime[i+1], '%Y-%m-%d %H:%M:%S.%f')
            delta = (item2 - item1)
            list_delta.append(delta.total_seconds())
            j += 1
            i += 2
        # print('len delta = ',len(list_delta))
        list_index = [1, 2, 3, 4, 5]
        myclass.dfprime.index = list_index
        myclass.dfprime['Marche panneau vichy'] = list_delta[0:5]
        myclass.dfprime['Marche panneau vichy[I]'] = list_delta[5:10]
        myclass.dfprime['Ramassage cube'] = list_delta[10:15]
        myclass.dfprime['Ramassage cube[I]'] = list_delta[15:20]
        myclass.dfprime['Dessin'] = list_delta[20:25]
        myclass.dfprime['Dessin[I]'] = list_delta[25:30]
        print(myclass.dfprime)
        return (myclass.dfprime.to_dict('records'), [{"name": i, "id": i} for i in myclass.dfprime.columns])


# @app.callback(
#     Output("green", "n_clicks"), Output("greenprime", "n_clicks"),
#     Input(component_id='button_reset', component_property='n_clicks')
# )

# def reset(n_clicks):
#     print('nclick reset = ', n_clicks)
#     if n_clicks > 0:
#         myclass.list_t.clear()
#         myclass.list_time.clear()
#         myclass.list_tprime.clear()
#         myclass.list_timeprime.clear()
#         return (n_clicks-1)

@app.callback(
    Output("green", "n_clicks"), Output("greenprime", "n_clicks"), Output(component_id='button_reset', component_property='n_clicks'),
    Output(component_id='precedent', component_property='n_clicks'),
    Output(component_id='precedentprime', component_property='n_clicks'),
    Input(component_id='button_reset', component_property='n_clicks'),
    Input(component_id='precedent', component_property='n_clicks'),
    Input(component_id='precedentprime', component_property='n_clicks')
)

def ft_precedent(n_clicks_reset, n_clicks, n_clicksprime):
    print('reset nclick = ', n_clicks_reset)
    print('precedent nclick = ', n_clicks)
    if n_clicks_reset != None:
        myclass.list_t.clear()
        myclass.list_time.clear()
        myclass.list_tprime.clear()
        myclass.list_timeprime.clear()
        return (0, 0, None, None, None)
    if n_clicks != None:
        myclass.list_t = myclass.list_t[:-2]
        myclass.list_time = myclass.list_time[:-2]
        return (0, 0, None, None, None)
    if n_clicksprime != None:
        myclass.list_t = myclass.list_tprime[:-2]
        myclass.list_timeprime = myclass.list_timeprime[:-2]
        return (0, 0, None, None, None)

@app.callback(
    Output("modal", "is_open"),
    [Input("button", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1 and len(myclass.list_time) < 50:
        return True
    return False

@app.callback(
    Output("modalprime", "is_open"),
    [Input("buttonprime", "n_clicks")],
    [State("modalprime", "is_open")],
)
def toggle_modal(n1, is_open):
    if n1 and len(myclass.list_timeprime) < 50:
        return True
    return False

if __name__ == "__main__":
    app.run_server(debug=True)