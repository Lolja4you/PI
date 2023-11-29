import random

import tkinter as tk
from tkinter import messagebox

import utils 

class DescreteSpace:
    def __init__(self, sizes:tuple) -> None:
        self.sizes = sizes
        self.paths: dict = {}
        self.nodes = {}
        self.connection = {}
    
    def create_node(self):
        if 2 >= utils.get_last_pk(self.nodes):
        # if 0.2 >= utils.get_last_pk(self.nodes)/(self.sizes[0]*self.sizes[1]): 
            node = (round(random.randint(0, self.sizes[0]-25)/25)*25, round(random.randint(0, self.sizes[1]-25)/25)*25) # (x,y)
            if not self.is_valid_node(node):
                node = self.create_node()
            else:
                pk = utils.get_last_pk(self.nodes)+1
                self.nodes[pk] = Node(is_main=True, x=node[0], y=node[1], pk=pk)
                return f'succes: ({node[0]} {node[1]})'
                
        else:
            return "Невозможо создать еще одну точку"

    def is_valid_node(self, node):
        for i in self.nodes:
            if i == node:
                return False   
        return True
    
    def input_node(self, message):
        try:
            node =  int(input(f"введите {message} компонент: "))
            return node
        except ValueError:
            self.input_node(message)

    def add_connection(self, nodes):
        first_node, last_node  = nodes
        if not self.is_valid_connection(first_node, last_node):
            messagebox.showerror("Ошибка", 'некорректные данные')
            print("некорректные данные")
            return
        else:
            self.check_node_in_adjacency_dict(first_node, self.connection)
            self.connection[first_node].append(last_node) 
        print('Соединения схемы: ', self.connection)

    def UI_input_connection(self):   
        print(self.nodes) 
        root = tk.Tk()
        root.title("message")

        x_label = tk.Label(root, text=f"Укажите начальную точку:")
        x_label.pack()
        x_entry = tk.Entry(root)
        x_entry.pack()

        y_label = tk.Label(root, text=f"Укажите конечную точку:")
        y_label.pack()
        y_entry = tk.Entry(root)
        y_entry.pack()

        def get_tuple():
            x = x_entry.get()
            y = y_entry.get()
            try:
                x = self.nodes[int(x)]
                y = self.nodes[int(y)]
            except KeyError:
                messagebox.showerror('Ошибка', "такого компонента не существует")
                root.destroy()
                return 1

            self.add_connection((x,y))
            root.destroy()


        add_button = tk.Button(root, text="ок", command=get_tuple)
        add_button.pack()
        root.mainloop()

    def check_node_in_adjacency_dict(self, node, circuit):
        try:
            circuit[node]
        except KeyError:
            circuit[node] = []

    def is_valid_connection(self, first_node, last_node):
        if first_node == last_node:
            print("components equal")
            messagebox.showerror("Ошибка", "components equal")
            return False
        elif (first_node or last_node) in self.nodes.items():
            print(f"такого компонента не существует {not (first_node or last_node) in self.nodes} {not (first_node or last_node) in self.nodes.items()}")
            print(f"{first_node} {last_node}\n{self.nodes}")
            messagebox.showerror('Ошибка', "такого компонента не существует")
            return False
        
        for i in self.connection:
            id_list = [i]
            for el in self.connection[i]:
                id_list.append(el)
            try:
                id_list.index(first_node)
                id_list.index(last_node)
                messagebox.showerror('Ошибка', "такое соединение существует")
                return False
            
            except ValueError:...

        return True

    def get_percentage_of_filling(self):
        percent = utils.get_last_pk(self.nodes)/(self.sizes[0]*self.sizes[1])
        return percent
    
    def show_paths(self):
        for key, item in self.paths.items():
            print(key, item)
    
    def reset(self):
        self.paths: dict = {}
        self.nodes = {}
        self.connection = {}


class Node:
    def __init__(
            self,
            x:int,y:int,pk:int,
            is_main:bool=False,
    ) -> None:
        
        self.is_main = is_main
        self.x = x
        self.y = y
        self.pk = pk
        self.weight = 0