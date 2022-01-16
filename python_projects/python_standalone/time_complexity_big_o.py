
# order of n example o(n)

def get_squared_numbers(numbers):
    squared_numbers = []
    
    for number in numbers:
        squared_numbers.append(number*number)
    

    return squared_numbers

numbers = [4, 3, 2, 1]

print(get_squared_numbers(numbers))


# order of 1 example o(1)
# doesn't affect the time complexity due to the size of an array

def get_first_pe(stock_prices, eps, index):
    pe = stock_prices[index]/eps[index]
    print(pe)
    return pe

get_first_pe([15600, 200], [5600, 100], 1)

# find dupllicates from a list
# complexity n^2

list_numbers = [3, 5, 6, 3, 4, 5]

for i in range(len(list_numbers)):
    for j in range(i+1, len(list_numbers)):
        if list_numbers[i] == list_numbers[j]:
            print(str(list_numbers[i]) + " is a duplicate")
            break

# another example with n^2 + n but considered as n

another_list_numbers = [3, 2, 5, 6, 8, 5, 7, 3, 9, 9, 9]
duplicate = None

for i in range(len(another_list_numbers)):
    for j in range(i+1, len(another_list_numbers)):
        if another_list_numbers[i] == another_list_numbers[j]:
            duplicate = another_list_numbers[i]
            print(duplicate)
            break

for i in range(len(another_list_numbers)):
    if another_list_numbers[i] == duplicate:
        print(i)
        print(str(i) + " is duplicate")

# some simple array operations

array_numbers = [1, 2, 4, 5, 6, 3, 21, 34, 54, 89, 9]

array_numbers.insert(4, 56)
print(array_numbers)
array_numbers.remove(6)

array_numbers.pop(1)
print(array_numbers)

# binary search example

# list_range = len(array_numbers)

# for i in l/list_numbers: 

# Two dimentional array example

prices = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(prices[1][1])