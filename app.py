# import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/faeldon/philippines-json-maps/master/geojson/regions/lowres/regions.0.001.json') as response:
    regions = json.load(response)

regions["features"][0]


# reading the data from the Bureau of Fire Protection Fire Incidents Dataset
df = pd.read_excel('data.xlsx', # file name
                   sheet_name='FIRE INCIDENTS', #specifying the target excel sheet
                   skipfooter=1) #disregard the footer row which is the total 

# initialize the app / dash constructor
app = Dash(__name__)

# app components will be displayed in the web browser
app.layout = html.Div([
    html.H1(children='Fire Incidents in the Philippines'),
    html.Hr(),
    # represents the yearly data of the fire incidents
    # dcc dropdown component
    dcc.Dropdown(id='year-dropdown',
                 options=[
                     {"label": "2010", "value": 2010},
                     {"label": "2011", "value": 2011},
                     {"label": "2012", "value": 2012},
                     {"label": "2013", "value": 2013},
                     {"label": "2014", "value": 2014},
                     {"label": "2015", "value": 2015},
                     {"label": "2016", "value": 2016},
                     {"label": "2017", "value": 2017},
                     {"label": "2018", "value": 2018},
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021}],
                 multi=False,
                 value=2021, #default selected value
                 style={"width": "30%"}
                  ),
    # data table 
    #dash_table.DataTable(data=df.to_dict('records'), page_size=20),
    # render interactive graph
    dcc.Graph(figure={}, id='controls-and-graph'),
    ]) 

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)

def update_graph(col_chosen):
    fig = px.histogram(df, x='REGION', y=col_chosen, histfunc='avg')
 
    return fig


# run the app
if __name__ == '__main__':
    app.run_server(debug=True)