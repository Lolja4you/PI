from .draw_classes import DrawNode, DrawWire, DrawResisrtor
from main_class import space


components_dict = space.nodes

def components_drawer(canvas, components_dict=components_dict):
    components = []
    for component in components_dict:
        x = components_dict[component][0] * 200 + 50
        y = components_dict[component][1] * 200 - 80
        length = 50
        angle = 0
        color = "black"
        components.append(DrawResisrtor(canvas, x=x, y=y, length=length, angle=angle, color=color))
    return components