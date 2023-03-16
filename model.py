"""model.py - Create a simple model that does nothing

Created by R. Ramsdell 2023-03-16
"""

from mesa_geo import GeoSpace, GeoAgent, AgentCreator
from mesa import Model, Agent
from mesa.time import BaseScheduler


class DoNothing(Model):
    """DoNothing - A model that does nothing"""
    def __init__(self):
        Model.__init__(self)
        self.space = GeoSpace(crs='epsg:2278')
        self.schedule = BaseScheduler(self)

    def step(self):
        pass
