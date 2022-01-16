def solution():

    my_list = [[2, 4], [2, 6], [2, 8], [2, 4]]
    # my_set = set()
    # for l in my_list:
    #     for e in l:
    #         my_set.add(e)
    uniques = set(tuple(arr) for arr in my_list)
    num_unique = len(uniques) if () not in uniques else len(uniques) - 1

    print(uniques)
    print(num_unique)
solution()