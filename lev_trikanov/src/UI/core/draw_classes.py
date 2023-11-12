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
    def __init__(self, canvas, x: int, y: int, color: str = 'silver', length: int = 0, angle: int = 0):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.length = length
        self.angle = angle
        self.__radius = 10
        self.__width = 3

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


class DrawResisrtor(DrawNode):
    def __init__(self, canvas, x, y, color='#595959', length=0, angle=0):
        super().__init__(canvas, x, y, color, length, angle)

    def draw(self):
        left_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y,
            length=40, angle=90+self.angle, 
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        bottom_border = DrawWire(
            self.canvas, 
            x=self.x, y=self.y, 
            length=100, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )

        top_border = DrawWire(
            self.canvas, 
            left_border.x2, left_border.y2, 
            length=100, angle=self.angle,
            is_node_1=False, is_node_2=False, 
            color=self.color
        )
        right_border = DrawWire(
            self.canvas, 
            bottom_border.x2, 
            bottom_border.y2, 
            length=40, angle=90+self.angle, 
            is_node_1=False, is_node_2=False,
            color=self.color
        )
        
        left_border.draw()
        bottom_border.draw()

        top_border.draw()
        right_border.draw()

        left_conductor = DrawWire(
            self.canvas, 
            left_border.x1+(left_border.x2-left_border.x1)/2, 
            left_border.y1+(left_border.y2-left_border.y1)/2, 
            length=-50, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        left_conductor.draw()

        right_conductor = DrawWire(
            self.canvas, 
            right_border.x1+(right_border.x2-right_border.x1)/2, 
            right_border.y1+(right_border.y2-right_border.y1)/2, 
            length=50, angle=self.angle, 
            is_node_1=False, is_node_2=True,
            color=self.color
        )
        right_conductor.draw()
    def move(self, dx, dy):
        super().move(dx, dy)
    