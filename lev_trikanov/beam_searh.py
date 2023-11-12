

def beam_search_initialization(space):
    for i in space.connection:
        text = f"""
                
                connection(1st:2nd) {i} : {space.connection[i]}
                components:         {space.nodes[i]} 

               """ 
        print(text)
        start_A = space.nodes[i]
        for el in space.connection[i]:
            start_B = space.nodes[el]
            beam_search(space, start_A, start_B)
    


def beam_search(space, start_A, start_B):
    path_a = []
    path_b = []
    Ax_current, Ay_current = start_A
    Bx_current, By_current = start_B
    
    while True:
        if Ax_current == Bx_current and Ay_current == By_current:
            print(path_a, path_b)
            break
        elif Ax_current == start_B[0] and Ay_current == start_B[1] or Bx_current == start_A[0] or By_current == start_A[1]:
            print(path_a, path_b)
            break
        else:
            print(1)
            for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                Ax_current += dx; Ay_current += dy
                Bx_current += dx; By_current += dy
                path_a.append((Ax_current, Ay_current))
                path_b.append((Bx_current, By_current))
                print(path_a, path_b)

    