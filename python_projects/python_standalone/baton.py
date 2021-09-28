def baton(friends, time): # 4, 1

    friends_range = range(friends)
    if (time<friends):
        output = friends_range[time:time+1]
        return output
    time_one_way = friends - 1 #3   
    remaining_time = time - time_one_way
    output = None
    calculate_traverse_side = time/time_one_way
    if (time%time_one_way == 0):
        if (calculate_traverse_side%2 == 0):
            output = friends_range[2:1]
            return output
        output = friends_range[friends-1:friends]
        return output
    remainder = time%time_one_way
    print(remainder)
    if (calculate_traverse_side%2 == 0):
        output = friends_range[remainder:remainder+1]
        return output
    output = friends_range[friends-(remainder-1):friends-remainder]
    return output

print(baton(7, 10))

# 1 2 3 4 5
# 4 5 6 7 8 9 10 11 12   