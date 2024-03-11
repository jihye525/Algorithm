from collections import deque
def solution(numbers, target):
    n = len(numbers)
    sum_list = [numbers[0], -numbers[0]] 
    
    for i in range(1, n):
        temp = []
        for v in sum_list:
            temp.append(v + numbers[i])
            temp.append(v - numbers[i])
           
        sum_list = temp    
    return sum_list.count(target)


