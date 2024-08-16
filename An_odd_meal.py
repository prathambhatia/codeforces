def meals(array):
    curr_sum = sum(array)
    n = len(array)
    
    if curr_sum % 2 != 0:
        return n
    
    first_odd_index = -1
    last_odd_index = -1
    
    for i in range(n):
        if array[i] % 2 != 0:
            if first_odd_index == -1:
                first_odd_index = i
            last_odd_index = i
    
    if first_odd_index == -1:
        return -1
    
    return max(n - first_odd_index - 1, last_odd_index)
 
n = int(input())
array = list(map(int, input().split()))
print(meals(array))
