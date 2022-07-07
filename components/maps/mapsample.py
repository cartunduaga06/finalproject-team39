from dash import html , dcc
import plotly.express as px
import plotly.graph_objects as go


class mapsample:    
    """A class to represent a samplemap of Montreal Elections"""        
    def __init__(self,map_title:str,ID:str, df):
        """__init__
        Construct all the attributes for the sample map
     
        Args:
            map_title (str): _Title for the map_
            ID (str): _div id to specify unique #id with callbacks and css_
        
        Methods:

        display()
            Function to display a sample map with no arguments, uses plotly express data.
            
            Arguments:
                None

            Returns:
                html.Div : A Div container with a dash core component dcc.Graph() inside
        """
        
        self.map_title = map_title
        self.id = ID
        self.df = df

    @staticmethod
    def figura(self):
         
        #df = px.data.election() # replace with your own data source
        #geojson = px.data.election_geojson()
        import json
        with open ('./data/jsonmaps/famanecer_municipios.json') as json_file:
            geojson = json.load(json_file)
        print(geojson['features'][5])
        fig = px.choropleth(
             self.df, geojson=geojson, #color="Nro Solicitud",
             #color_continuous_scale="Viridis",
             locations="Sucursal Real", featureidkey="properties.MPIO_CNMBR",
             #projection="mercator"                 
            )

        #fig = go.Figure(go.Choroplethmapbox(
        #    geojson=geojson, 
        #    locations=self.df['Sucursal Real'], 
        #    featureidkey="properties.id",
        #    z=self.df['Sucursal Real'],
        #    colorscale="dense",
        #    text=self.df['Sucursal Real'],
        #    marker_opacity=0.9, 
        #    marker_line_width=0.5,
        #    colorbar_title = "COP",
        #    ))

        annotations = [
            dict(
                showarrow=False,
                align="right",
                text="",
                font=dict(color="#000000"),
                bgcolor="#f9f9f9",
                x=0.95,
                y=0.95,
            )
        ]
        fig.update_layout(
            #geo_scope='south america',
            #mapbox_style="carto-positron",
            mapbox_zoom=5.5, 
            mapbox_center = {"lat": 4.570868, "lon": -74.2973328},
            annotations=annotations,
            height=1000),

        #fig.update_layout(mapbox_style="open-street-map")
        #fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
        
        fig.update_geos(fitbounds="locations")

        return fig

    def display(self):
       
        layout = html.Div(
            [
                html.H4([self.map_title]),
                html.Div([
                    dcc.Graph(figure=self.figura(self))
                ])
                
            ],id=self.id
        )
        return layout

