from utils import get_direction

def beam_search_initialization(space):
    for key_main_point, seconds_points in space.connection.items():
        text = f"""
                connection(1st:2nd) {key_main_point} : {seconds_points}
               """ 
        print(text)
        start_A = (key_main_point.x, key_main_point.y)
        for el in seconds_points:
            start_B = (el.x, el.y)
            print(start_A, start_B)
            beam_search_result = beam_search(space, start_A, start_B)
            space.paths[f'{key_main_point.pk} : {el.pk}'] = beam_search_result
    

def beam_search(space, start_A, start_B):
    traversal = [] #путь пройденных точек по ним мы восстановим путь [(25,0), (50, 0), (75, 0)]
    x_a, y_a = start_A # x_a, y_a <= (x, y)
    x_b, y_b = start_B
    cur_direction, length = get_direction(x_a, y_a, x_b, y_b)

    while True:
        print(length)
        print(cur_direction)
        for i in range(0, length, 25):
            x_a += cur_direction[0]
            y_a += cur_direction[1]
            if x_a == x_b and y_a == y_b:   
                print(traversal)
                       
                return traversal
            traversal.append((x_a, y_a))
        cur_direction, length = get_direction(x_a, y_a, x_b, y_b)
        print(traversal)
        if x_a == x_b and y_a == y_b:
            break
        input()

    
