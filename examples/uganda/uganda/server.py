import mesa
from shapely.geometry import Point, Polygon

from mesa_geo.geoagent import GeoAgent
from mesa_geo.visualization.ModularVisualization import ModularServer
from mesa_geo.visualization.modules import MapModule

from .model import Uganda
from .space import UgandaCell


class NumAgentsElement(mesa.visualization.TextElement):
    def __init__(self):
        super().__init__()

    def render(self, model):
        return f"Number of Agents: {len(model.space.agents)}"


def agent_portrayal(agent):
    if isinstance(agent, GeoAgent):
        if isinstance(agent.geometry, Point):
            return {
                "stroke": False,
                "color": "Green",
                "radius": 2,
                "fillOpacity": 0.3,
            }
        elif isinstance(agent.geometry, Polygon):
            return {
                "fillColor": "Blue",
                "fillOpacity": 1.0,
            }
    elif isinstance(agent, UgandaCell):
        return (agent.population, agent.population, agent.population, 1)


geospace_element = MapModule(agent_portrayal)
num_agents_element = NumAgentsElement()

server = ModularServer(Uganda, [geospace_element, num_agents_element], "Uganda Model")
