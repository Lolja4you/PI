from .draw_classes import UnkownComponents

def components_drawer(canvas, components_dict):
    components = []
    for key, component in components_dict.items():
        try:
            x = component.x
            y = component.y
            components.append(UnkownComponents(canvas, x=x, y=y, pk=component.pk, color='red'))
        except AttributeError:
            for i in component:
                x = i[0]
                y = i[1]
                components.append(UnkownComponents(canvas, x=x, y=y, color='gray'))
    return components