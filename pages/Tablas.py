import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins.pages import register_page
import  pandas  as pd


from components.table.table import *
from components.sampledf.model import df_costos, df_opsales,  df_carteraCombinada

data3 =  pd.DataFrame()
data3['Region'] = df_carteraCombinada['Region']
data3['Monto'] = df_carteraCombinada['Monto']
data3['Tipo Credito'] = df_carteraCombinada['Tipo Credito']
data3['Año'] = df_carteraCombinada['Año']
data3['Dias vencido'] = df_carteraCombinada['Dias vencido']

register_page(__name__, path="/tablas")

        


params = {
            'title': 'Cartera Combinada',
            'description': 'Tabla de lista de cartera combinada',
            'columns': ['Region','Monto','Tipo Credito','Año','Dias Vencido'] #['Tipo','Nro Solicitud','Obligacion,Pagare','Homologacion Documento de Identidad','Cod tipo Cliente','Nom tipoCliente','Sucursal Real,Region','Fec solicitud','Fec Aproba','Fec Desembolso','Cuotas pactadas','Cuotas pendientes','Tasa N.A.M.V','Tasa Periodica','Periodicidad','Calificacion Cierre','Cod Linea','Linea','Cod modalidad','Modalidad', 'Vencida' ,'Dias vencido', 'Capital Ven' , 'Interes Ven' , 'Mora' , 'Seguro Vida ','Fec ult.Pago','Fec Proximo Pago','Vencimiento Final','Garntia real','Porcentaje pago','Tipo Credito','Sucurs','Mes','Año','Monto','Valor cuota','state_date','Comision','ubicacion_cliente','saldo_obligacion']
}



tablacartera = table(data3, params)

layout= dbc.Container([
    
    
    dbc.Row([
        dbc.Col([
            tablacartera.display()
        ])
    ], className= "card")
])
