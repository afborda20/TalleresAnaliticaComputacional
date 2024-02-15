# -*- coding: utf-8 -*-

# Ejecute esta aplicación con 
# python app1.py
# y luego visite el sitio
# http://127.0.0.1:8050/ 
# en su navegador.

import dash
from dash import dcc  # dash core components
from dash import html # dash html components
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# en este primer ejemplo usamos unos datos de prueba que creamos directamente
# en un dataframe de pandas 
data = {
    "Año": [2020, 2020, 2021, 2021, 2022, 2022],
    "Ganador": ["Egan Bernal", "Tadej Pogacar", "Tadej Pogacar", "Tadej Pogacar", "Primož Roglič", "Egan Bernal"],
    "Nacionalidad": ["Colombia", "Eslovenia", "Eslovenia", "Eslovenia", "Eslovenia", "Colombia"]
}
df_tour_de_francia = pd.DataFrame(data)
# Calcular el número de victorias por país
victorias_por_pais = df_tour_de_francia['Nacionalidad'].value_counts().reset_index()
victorias_por_pais.columns = ['País', 'Victorias']
colores_pais = {
    "Colombia": "yellow",
    "Eslovenia": "purple"
}
# Agregamos la ruta de las banderas al DataFrame
victorias_por_pais['Color'] = victorias_por_pais['País'].map(colores_pais)
fig = px.bar(victorias_por_pais, x='País', y='Victorias', 
             color='País', color_discrete_map=colores_pais,
             labels={'País': 'País', 'Victorias': 'Número de Victorias'}, 
             hover_data=['Victorias'],
             title='Victorias en el Tour de Francia por País')

# Personalizar el diseño del gráfico
fig.update_layout(xaxis_title="País", yaxis_title="Número de Victorias", legend_title="Países")

app.layout = html.Div(children=[
    html.H1(children='Mi primer tablero en Dash'),

    html.Div(children='''
        Datos de ganadores del tour de francia segun paises por año
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        En este gráfico se observan los ganadores de los ultimos 4 años del tour de france.
    '''),
    html.Div(
        className="Columnas",
        children=[
            html.Ul(id='my-list', children=[html.Li(i) for i in df_tour_de_francia.columns])
        ],
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
