"""server.py - Show the various layers of an ENC nav chart in a mesa browser window"""
import os

from mesa.visualization.ModularVisualization import ModularServer
from mesa_geo.visualization import MapModule
import xyzservices.providers as xyz
from mesa_geo.tile_layers import WMSWebTile
from mesa.visualization.modules import TextElement

from model import DoNothing

map_width = 1000

# Providers for the tiles parameter here:
# https://github.com/geopandas/xyzservices/blob/main/provider_sources/xyzservices-providers.json
# Asked for help here: https://github.com/projectmesa/mesa-geo/discussions/139
map_tiles = {"paper": WMSWebTile(url="https://gis.charttools.noaa.gov/arcgis/rest/services/MCS/NOAAChartDisplay/MapServer/exts/MaritimeChartService/WMSServer/",  # "https://gis.charttools.noaa.gov/arcgis/rest/services/MCS/ENCOnline/MapServer/exts/MaritimeChartService/WMSServer",
                                       options={"layers": "0,1,2,3,4,5,6,7,8,9,10,11,12",
                                                # "version": "1.3.0",
                                                "attribution": '&copy; <a href="https://www.nauticalcharts.noaa.gov/">NOAA</a>',
                                                "transparent": True
                                                },
                                       ),
             "enc": WMSWebTile(url="https://gis.charttools.noaa.gov/arcgis/rest/services/MCS/ENCOnline/MapServer/exts/MaritimeChartService/WMSServer",
                                     options={"layers": "0,1,2,3,4,5,6,7,8,9,10,11,12",
                                              # "version": "1.3.0",
                                              "attribution": '&copy; <a href="https://www.nauticalcharts.noaa.gov/">NOAA</a>',
                                              "transparent": True
                                              },
                                     ),
             "street": xyz.OpenStreetMap.Mapnik
             }


class LayerLabel(TextElement):
    """Show the scenario results"""
    def __init__(self, layer=None, chart_type=None):
        self.layer = layer
        self.chart_type = {'paper': "Paper Chart",
                           'enc': "ENC Chart",
                           'street': "Open Map"}

    def render(self, model):

        return '\n'.join([f'Chart Type: {self.chart_type}',
                          f'Layer: {self.layer}'])


def server(layers=None, chart_type="paper"):
    if layers is None:
        layers = "1,2,3,5"  # The best combination I've found

    tiles = map_tiles[chart_type]
    tiles.options["layers"] = layers

    map_mod = MapModule(view=[29.5, -94.875],
                        zoom=10,  # center window on a point in Galveston bay
                        map_height=1000,
                        map_width=1000,
                        tiles=tiles,
                        scale_options={})

    map_elements = [LayerLabel(layers),
                    map_mod]

    return ModularServer(DoNothing,
                         map_elements,
                         "NOAA Web Chart Layers")
