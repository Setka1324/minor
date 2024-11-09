def sumodd(numbers):

    summ_odd = 0

    for i in numbers:
        if i % 2 == 1:
            summ_odd += i

    return summ_odd

def reverse_list(lst):
    
    return[lst[::-1]]


def longest_repetition(lst):
    
    max_count = 1
    current_count = 1

    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current_count += 1
        else:

            if current_count > max_count:
                max_count = current_count
            
            current_count = 1
    return max_count



def combine_dicts(dict1, dict2):

    final = dict1

    for i in dict2.keys():
        if i in final:
            final[i] = [final[i], dict2[i]]
        else:
            final[i] = dict2[i]

    return final

def newtons_method_square_root_t(n, threshold):

    root = n

    while abs(root ** 2 - n) > threshold:
        root = 0.5 * (root + n / root)
    

    return root

def generate_1x1_grid(step):

    points = []
    i = 0
    while i <= 1:
        points.append(i)
        i += step

    grid = []

    for i in points:
        for z in points:
            grid.append((i, z))
    
    return grid


result = generate_1x1_grid(0.5)
print(result)