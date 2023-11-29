import tkinter as tk

from .draw_api import components_drawer
from main_class import DescreteSpace
from .tool_frame import ToolFrame

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.x = int(round(self.winfo_screenwidth()/50)*25)
        self.y = int(round(self.winfo_screenheight()/50)*25)
        self.title("test_1 - САПР")
        self.space = DescreteSpace(sizes=(self.x, self.y))

        self.geometry(f"{self.x}x{self.y}")
        self.resizable(height = False, width = False)

        self.canvas = tk.Canvas(self, width=self.x, height=self.y, bg="#ffffff") ##fff9f7
        self.canvas.pack()

        '''
        tool frame
        '''
        self.tool_frame = ToolFrame(self, self.x, self.space)
        self.tool_frame.place(x=self.x - (self.x*1) + 10, y=10)


        self.canvas.focus_set()

        self.workspace_width = self.x
        self.workspace_height = self.y
        self.quadrant_size = 200
        self.subsquare_size = self.quadrant_size // 8

        
        self.x_offset = 0
        self.y_offset = 0
        
        self.canvas.bind("<Motion>", lambda event: (self.update_cursor_position(event),))

        self.cursor_position_x = tk.StringVar()
        self.cursor_position_y = tk.StringVar()

        '''
        cursor position
        '''
        self.cursor_position_label = tk.Label(self, textvariable=self.cursor_position_x)
        self.cursor_position_label.place(x=10, y=self.y-120)

        self.cursor_position_label2 = tk.Label(self, textvariable=self.cursor_position_y)
        self.cursor_position_label2.place(x=10, y=self.y-100)


        self.draw_subsquare()
                
        '''
        initial drawing components
        '''
        self.node = components_drawer(self.canvas, self.space.nodes)
        self.node += components_drawer(self.canvas, self.space.paths)
        for components in self.node:
            components.draw()

    def update_cursor_position(self, event):
        x = round((event.x+self.x_offset) / 25) * 25 
        y = round((event.y+self.y_offset) / 25) * 25 
        self.current_cursor_position_x = x
        self.current_cursor_position_y = y
        self.cursor_position_x.set(f"X: {x}")
        self.cursor_position_y.set(f"Y: {y}")

    def draw_subsquare(self, wrapped=False):
        for x in range(int(self.x_offset / self.subsquare_size), int((self.x_offset + self.workspace_width) / self.subsquare_size) + 1):
            for y in range(int(self.y_offset / self.subsquare_size), int((self.y_offset + self.workspace_height) / self.subsquare_size) + 1):
                x1 = x * self.subsquare_size - self.x_offset 
                y1 = y * self.subsquare_size - self.y_offset
                x2 = x1 - self.subsquare_size if wrapped else x1 + self.subsquare_size
                y2 = y1 - self.subsquare_size if wrapped else y1 + self.subsquare_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="#888888") #cfcfcf

    def redraw(self):
        self.draw_subsquare()
        for components in self.node:
            components.draw()

    def add_points(self):
        self.node += components_drawer(self.canvas, self.space.nodes)
    def draw_paths(self):
        self.node += components_drawer(self.canvas, self.space.paths)