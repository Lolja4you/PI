class DiscreteSpace:
    def __init__(self) -> None:
        self.n = 25
        self.discrete_space = self.creat_discrete_space()

        self.x_start: int = -999
        self.y_start: int = 999

        self.x_end: int = 999
        self.y_end: int = 999

    def creat_discrete_space(self):
        matrix = [[0 for _ in range(self.n)] for _ in range(self.n)]
        return matrix

    def create_elements_in_discrete_space(self):...

    def add_node(self, x,y, type_node):
        try:
            if 's' in type_node:
                self.discrete_space[self.y_start][self.x_start] = 0
            elif 'e' in type_node:
                self.discrete_space[self.y_end][self.x_end] = 0
        except IndexError:...
        self.discrete_space[y][x] = type_node

    def __str__(self) -> str:
        strings= ''
        for i in self.discrete_space:
            strings+=f'{i}\n'
        return strings

#######################################
#######################################
#######################################



def input_node():
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))
    return x, y


def choose_node(is_node):
    x,y = input_node()
    if is_node:
        x_end, y_end = is_valid_node(x, y, is_node)
        space.add_node(x_end, y_end, 'e')
        space.x_end = x_end
        space.y_end = y_end
    else:
        x_start, y_start = is_valid_node(x, y, is_node)
        space.add_node(x_start, y_start, 's')
        space.x_start = x_start
        space.y_start = y_start


def is_valid_node(x, y, is_node):
    if (space.x_end, space.y_end) == (space.x_start, space.y_start):
        print("Точки находятся на одной координате")
        
    return x,y

#######################################
#######################################
#######################################

def show_menu():
    menu =  """
        0)  Сгенерировать матрицу
        1)  Выбрать начальную точку
        2)  Выбрать конечную точку
        3)  случайный выбор точек

        *)  показать матрицу
        **) начать вычисления

        exit/quit выход из программы

        """
    print(menu)

def user_choose():
    choose = input("--> ")

    match choose:
        case "0": created_matrix()
        case "1": input_node(is_node=False)
        case "2": input_node(is_node=True)
        case "3": capacitor.input_capacitor_data(circuit_init)

        case "*": print(space.__str__())
        case "**": inductor.input_inductor_data(circuit_init)

        case "quit": return quit()  
        case "exit": return quit()


#######################################
space = DiscreteSpace()
#######################################


if __name__ == '__main__':
    while True:
        show_menu()
        user_choose()