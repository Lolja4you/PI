import tkinter as tk
from tkinter import ttk


from .UI_utils import DropdownButton
from beam_searh import beam_search_initialization


class ToolFrame(tk.Frame):
    def __init__(self, parent, width, circuit_init):
        self.parent = parent 
        self.circuit_init = circuit_init
        super().__init__(parent, borderwidth=2, relief="solid", width=width * 0.50, height=50, background='#484848')
        
        self.app_list = [
           DropdownButton(self, text='functions', 
                            button_commands=[
                                self.init_pathfinder,
                                self.add_node,
                                self.add_connection,
                                self.show_nodes,
                            ]
            ),

        ]
        for i, button in enumerate(self.app_list):
            button.column = i
            button.grid(row=0, column=i, sticky="nsew")

    def init_pathfinder(self):
        """pathfinder"""
        beam_search_initialization(self.circuit_init)
        self.parent.draw_paths()
        self.parent.redraw()
        print(self.parent.node)

    def add_connection(self):
        """add connection"""
        self.circuit_init.UI_input_connection()

    def add_node(self):
        """add node"""        
        message = self.circuit_init.create_node()
        print(message)
        if 'succes' in message:
            self.parent.add_points()
            self.parent.redraw()
    
    def show_nodes(self):
        """show nodes"""
        message = str(self.circuit_init.nodes)
        message += ' '
        message += str(self.circuit_init.get_percentage_of_filling())
        print(message)
