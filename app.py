from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


# reading the data from the Bureau of Fire Protection Fire Incidents Dataset
df = pd.read_excel('data.xlsx',
                   sheet_name='FIRE INCIDENTS', #specifying the target excel sheet
                   skipfooter=1) #disregard the footer row which is the total 

#
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Fire Incidents in the Philippines'),
    html.Hr(),
    dcc.Dropdown([2010,
                  2011,
                  2012,
                  2013,
                  2014,
                  2015,
                  2016,
                  2017,
                  2018,
                  2019,
                  2020,
                  2021],
                  2021,
                  id='year-dropdown'
                  ),
    #dash_table.DataTable(data=df.to_dict('records'), page_size=20),
    dcc.Graph(figure={}, id='controls-and-graph'),
    
    ]) 

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='year-dropdown', component_property='value')
)

def update_graph(col_chosen):
    fig = px.histogram(df, x='REGION', y=col_chosen, histfunc='avg')
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)