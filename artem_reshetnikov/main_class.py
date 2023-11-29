import random

import utils 

class DescreteSpace:
    def __init__(self) -> None:
        self.n = 6
        self.space = self.create_space() 
        self.nodes = {}
        self.connection = {}

    def create_space(self):
        return [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    def create_node(self):
        if 0.2 >= utils.get_last_pk(self.nodes)/(self.n**2): 
            node = (random.randint(0, self.n-1), random.randint(0, self.n-1)) # (x,y)
            if not self.is_valid_node(node):
                node = self.create_node()
            else:
                self.nodes[utils.get_last_pk(self.nodes)+1] = node
                self.space[node[1]][node[0]] = "x"
        else:
            print("Невозможо создать еще одну точку")

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

    def add_connection(self):
        print('Компоненты схемы: ', self.nodes)
        first_node = self.input_node("начальный")
        last_node = self.input_node("конечный")
        if not self.is_valid_connection(first_node, last_node):
            print("некорректные данные")
        else:
            self.check_node_in_adjacency_dict(first_node, self.connection)
            self.connection[first_node].append(last_node) 
        print('Соединения схемы: ', self.connection)

    def check_node_in_adjacency_dict(self, node, circuit):
        try:
            circuit[node]
        except KeyError:
            circuit[node] = []

    def is_valid_connection(self, first_node, last_node):
        if first_node == last_node:
            print("components equal")
            return False
        elif not first_node in self.nodes or not last_node in self.nodes:
            print("такого компонента не существует")
            return False
        
        for i in self.connection:
            id_list = [i]
            for el in self.connection[i]:
                id_list.append(el)
            try:
                id_list.index(first_node)
                id_list.index(last_node)
                return False
            
            except ValueError:...

        return True

    def __str__(self) -> str:
        str_space= ''
        for i in self.space:
            str_space+= f"{i}\n"
        return str_space
         
space = DescreteSpace()