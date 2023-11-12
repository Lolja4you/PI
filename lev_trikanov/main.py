from src.UI import start  
from main_class import space
from beam_searh import beam_search_initialization

def info_print():
    menu = """
            1) показать пространство
            2) добавить компонент в случайное место
            3) запустить графическое окно
            4) добавить соединение
            5) найти путь

            выйти из программы exit/quit
    
           """
    print(menu)


def user_input():
    choose = input("--> ")
    
    match choose:
        case "1": print(space.__str__())
        case "2": space.create_node()
        case "3": start.init_UI()
        case "4": space.add_connection()

        case "5": beam_search_initialization(space)

        case "exit":return quit()
        case "quit":return quit()



if __name__ == '__main__':
    while True:
        start_component = 1  # Change this to the desired start component
        end_component = 2  # Change this to the desired end component
        beam_width = 1  # Change this to the desired beam width

        info_print()
        user_input()

        