import math


def get_last_pk(dictionary):
    pk_list = list(dictionary.keys())
    if len(pk_list) == 0:
        last_pk = 0
    else:
        last_pk = pk_list[-1]

    return int(last_pk)

def calculate_angle(x1, y1, x2, y2):
    y1 *= -1
    y2 *= -1
    angle = math.atan2(y2 - y1, x2 - x1)
    deg_angle = math.degrees(angle)
    if deg_angle < 0:
        deg_angle = 180 + abs(deg_angle)
    return deg_angle

def  get_direction(x_a, y_a, x_b, y_b) -> tuple:
    '''return (cur_direction, o_type, length)'''

    cur_direction = None
    distance = None
    o_type = None

    x_direction = (25, 0) #(x,y)
    x_neg_direction = (-25, 0)
    y_neg_direction = (0, 25) #(x,y)
    y_direction = (0, -25)

    length = x_a - x_b
    height = y_a - y_b
    
    if abs(length) < abs(height):
        if height < 0: #надо спуститься вниз y_direction= 25 
            cur_direction = y_neg_direction
        elif height > 0: #надо подняться наверх y_direction = -25
            cur_direction = y_direction
        else:...
        distance = abs(height)
    elif abs(length) > abs(height):
        if length < 0:
            cur_direction = x_direction #надо догнать справа x_direction = 25
        elif length > 0:
            cur_direction = x_neg_direction #надо догнать слева x_direction = -25
        else:...
        distance = abs(length)
    else:
        if length < 0:
            cur_direction = x_direction
            distance = abs(length)
        elif length > 0:
            cur_direction = x_neg_direction
            distance = abs(length)
        elif height < 0:
            cur_direction = y_neg_direction
            distance = abs(height)
        elif height > 0:
            cur_direction = y_direction
            distance = abs(height)
     


    return (cur_direction, distance) 
