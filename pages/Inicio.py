from inspect import trace
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page

register_page(__name__, path="/")
import dash_core_components as dcc
from components.kpi.kpibadge import kpibadge
from components.kpi.kpiplot import kpiplot
from components.table.table import table
import pandas as pd
import plotly.graph_objects as go
from components.sampledf.model import df_carteraCombinada
from components.maps.mapsample import mapsample
from pages.Tablas import tablacartera

data = df_carteraCombinada
tipoCLiente =  data['Nom tipoCliente'].value_counts()

#el valor de la cartera vencida total

data[' Vencida '] = data[' Vencida '].str.replace('-', '0').str.strip().astype(str)
data[' Vencida '] = data[' Vencida '].str.replace(',', '').str.strip().astype(float)

# cartera vencida por año 2021
total_df_vencida = data.groupby(data['Año']).sum()
vencida2020 =  total_df_vencida['saldo_obligacion'][2020]



kpi3plot = kpibadge('Urbano 463.789', 'Clasificación Cliente',  'Aproved')

kpi4plot = kpibadge('Rural 326.843', 'Clasificación Cliente',  'Aproved')

kpi5plot = kpibadge('Region Sur 161.670', 'Region',  'Aproved')

kpi6plot = kpibadge('Yopal 143.076 ', 'Sucursal',  'Aproved')
# kpi7plot = kpibadge('Total User', df_costos['VALUE'], 'count')

kpi1 = kpibadge(vencida2020, 'Total Cartera  2020', 'Danger')
kpi2 = kpibadge('A    665011', 'Calificacion cierre', 'Approved')
kpi3 = kpibadge('B     20835', 'Calificacion cierre', 'Approved')
kpi4 = kpibadge('C     13755', 'Calificacion cierre', 'Approved')
kpi5 = kpibadge('D     11164', 'Calificacion cierre', 'Approved')

mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

params1 = {
            'title': 'Cartera', 
            'description': 'Tabla de Cartera',
            'columns': ['ID', 'CIUDAD', 'TIPO', 'FECHA']
}
# tablaventas = table(df_costos,params1)
# tablacartera = table(df_carteraCombinada, params1)

#cambiar monto (str) a float
data['Monto'] = data['Monto'].str.replace('-', '0').str.strip().astype(str)
data['Monto'] = data['Monto'].str.replace(',', '').str.strip().astype(float)


#crear una tabla dinamica
pv = pd.pivot_table(df_carteraCombinada, index=['Año'], values=['Monto'], columns=['Linea'], aggfunc=sum)

trace1 = go.Bar(x=pv.index, y=pv['Monto']['CRECER'], name='CRECER')
trace2 = go.Bar(x=pv.index, y=pv['Monto']['GERMINA'], name='GERMINA')
trace3 = go.Bar(x=pv.index, y=pv['Monto']['MI CASA'] , name='MI CASA ')
trace4 = go.Bar(x=pv.index, y=pv['Monto']['FIDELIZACION'] , name='FIDELIZACION')
trace5 = go.Bar(x=pv.index, y=pv['Monto']['CREDINEGOCIO'] , name='CREDINEGOCIO')
trace6 = go.Bar(x=pv.index, y=pv['Monto']['CONVENIO'] , name='CONVENIO ')
trace7 = go.Bar(x=pv.index, y=pv['Monto']['CREDITO DIGITAL'] , name='CREDITO DIGITAL')
trace8 = go.Bar(x=pv.index, y=pv['Monto']['GARANTIA REAL'] , name='GARANTIA REAL')
trace9 = go.Bar(x=pv.index, y=pv['Monto']['UNETE'] , name='UNETE')




layout=  dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                kpi3plot.display()
            ], className='card'),
              dbc.Col([
                kpi4plot.display()
            ], className='card'),
             dbc.Col([
                kpi5plot.display()
            ], className='card'),
             dbc.Col([
                kpi6plot.display()
            ], className='card')
        ]),
        dbc.Row([
            dbc.Col([
                mapa_ejemplo.display()


            ], md=8), 
            dbc.Col([
                dbc.Row([
                    dbc.Col([ kpi1.display()]),
                    dbc.Col([ kpi2.display()]),
                    dbc.Col([ kpi3.display()]),
                    dbc.Col([ kpi4.display()]),
                    dbc.Col([ kpi5.display()])
                    
                ]),
                
            ]), 
        ]),
       
        dbc.Row([
            dbc.Col([
                dcc.Graph(
                    id='example-graph',
                    figure={
                        'data': [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9],
                        'layout': {
                            'title': 'Totales por Linea de Credito',
                            'barmode': 'stack'
                        }
                    }
                )
            ], md=8),   
        ]),
         dbc.Row([
            dbc.Col([
              tablacartera.display()
          ], md=8),
            
         ])


        
        
      
    ],

    
)  