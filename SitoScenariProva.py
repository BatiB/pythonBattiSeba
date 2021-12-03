# SOURCES
# PER LA TABELLA
# Table Prova
# https://dash.plotly.com/datatable/data-formatting
# https://dash.plotly.com/datatable/style
# https://dash.plotly.com/datatable/conditional-formatting
# https://community.plotly.com/t/percentage-format-in-dash-data-table-multiplies-the-numbers-by-100/55612/4
# https://community.plotly.com/t/dcc-tab-how-to-insert-a-svg-icon-or-img-inside-a-dcc-tab-css/27514/4
# Immagini in tabella risolto (workaround): https://github.com/plotly/dash-table/issues/383 (gmail BB 17 nov 21)

# CLASS NAMES
#https://getbootstrap.com/docs/4.0/utilities/spacing/


# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 15:26:23 2021

@author: svitali
"""

import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc


## Parte scarico dati ETF e pulizia


app = dash.Dash(name = 'Batti')

app.layout = dbc.Container(
    [

    html.H1(id='H1', children='ETF DASHBOARD', style={'textAlign': 'center', 'marginTop': 40, 'marginBottom': 40}),
    html.H2(id='H2BestETF', children='Statistiche migliori ETF',
            style={'textAlign': 'left', 'marginTop': 40, 'marginBottom': 40}, className="mx-5")
    ]
    )


if __name__ == '__main__':
    app.run_server()