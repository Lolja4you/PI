def get_last_pk(dictionary):
    pk_list = list(dictionary.keys())
    if len(pk_list) == 0:
        last_pk = 0
    else:
        last_pk = pk_list[-1]

    return int(last_pk)
