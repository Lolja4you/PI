from src.UI import start  
from beam_searh import beam_search_initialization

def info_print():
    menu = """
            1) запустить графическое окно
            выйти из программы exit/quit
    
           """
    print(menu)


def user_input():
    choose = input("--> ")
    
    match choose:
        case "1": start.init_UI()
        case "exit":return quit()
        case "quit":return quit()



if __name__ == '__main__':
    while True:
        info_print()
        user_input()

        