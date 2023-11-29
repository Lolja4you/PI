import math


def rotate_line(x1, y1, angle, length) -> tuple:
    # the center of the lines is the lower left corner
    angle_rad = -1 * angle * math.pi / 180

    new_x1 = x1
    new_y1 = y1
    new_x2 = length
    new_y2 = new_y1

    new_x2 = x1 + length * math.cos(angle_rad)
    new_y2 = y1 + length * math.sin(angle_rad)

    return new_x1, new_y1, new_x2, new_y2

def spin_rotation(x1, y1, x2, y2, angle, length=0):
    angle_rad = -1 * angle * math.pi / 180

    x1 = x1 + length * math.cos(angle_rad)
    y1 = y1 + length * math.sin(angle_rad)
    x2 = x2 + length * math.cos(angle_rad)
    y2 = y2 + length * math.sin(angle_rad)

    return x1,y1,x2,y2


class DrawNode:
    def __init__(self, canvas, x: int, y: int, color: str = 'silver', length: int = 0, angle: int = 0, pk:int =0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.__radius = 10
        self.__width = 3
        self.pk = pk

    def draw(self):
        top_left_x = self.x - (self.__radius/2)
        top_left_y = self.y - (self.__radius/2)
        bottom_right_x = self.x + (self.__radius/2)
        bottom_right_y = self.y + (self.__radius/2)

        self.canvas.create_oval(
            spin_rotation(
                top_left_x, top_left_y, 
                bottom_right_x, bottom_right_y,
                length=self.length,
                angle=self.angle,
            ),
            fill=self.color,
        )

    def move(self, dx=None, dy=None):
        self.x += dx
        self.y += dy
        self.draw()

class DrawWire(DrawNode):
    def __init__(self, canvas, x, y, color='white', length=0, angle=0, is_node_1 = True, is_node_2 = True):
        super().__init__(canvas, x, y, color, length, angle)
        self.x1,self.y1,self.x2,self.y2 = rotate_line(self.x, self.y, angle=self.angle, length=self.length) 
        self.is_node_1 = is_node_1
        self.is_node_2 = is_node_2

    def draw(self):
        self.canvas.create_line(
            rotate_line(
                self.x, self.y, angle=self.angle, length=self.length
            ), 
            width=self._DrawNode__width, 
            fill=self.color,
        )
        if not self.is_node_1:...
        else: 
            node_1 = DrawNode(self.canvas, self.x, self.y, angle=self.angle)
            node_1.draw()
        if not self.is_node_2:...
        else:
            node_2 = DrawNode(self.canvas, self.x, self.y, length=self.length, angle=self.angle
            )
            node_2.draw()

    def move(self, dx, dy):
        super().move(dx, dy)


class UnkownComponents(DrawNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def draw(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+25, self.y+25, fill=self.color,outline="gray")
        self.canvas.create_text(self.x+12.5, self.y+12.5, text=str(self.pk), fill="white")