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
        case "0": node.input_node(circuit_init)
        case "1": source.input_source_data(circuit_init)
        case "2": resistor.input_resistor_data(circuit_init)
        case "3": capacitor.input_capacitor_data(circuit_init)

        case "*": inductor.input_inductor_data(circuit_init)
        case "**": inductor.input_inductor_data(circuit_init)

        case "quit": inductor.input_inductor_data(circuit_init)   
        case "exit": inductor.input_inductor_data(circuit_init)