a = [1,2,3]
# 1 , 0
# 2 , 1
# 3 , 2
# 1,2 , 0-1
# 2,3,  1-2
# 1,2,3 = 6 , 0-1-2

def find_count(min, max):
    array = a[min:max]
    if min == max:
        return array
    count = sum(array)
    return count


def max():
    """
    case 1: a[0], a[0]     a[0], a[1]    a[0], a[2]
    case 2: a[1], a[1]     a[1], a[2]
    case 3: a[2], a[2]
    """
    # find a max sum of all the continuous sub arrays from array of integers
    array_length = len(a)
    temp = []
    # iterate over the array length
    for i in range(0, array_length):
        for j in range(i, array_length):
            max_count = find_count(i, j)
            temp.append(max_count)
    print(temp)
max()
