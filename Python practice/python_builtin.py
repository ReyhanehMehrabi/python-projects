import builtins

print(dir(builtins))


def average_function(list_of_numbers):
    total = sum(list_of_numbers)
    

    size_of_list = len(list_of_numbers)
    avg = total / size_of_list
    print(avg)

list_of_numbers = [2,4,6,8]

average_function(list_of_numbers)

