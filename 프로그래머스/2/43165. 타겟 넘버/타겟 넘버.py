def solution(numbers, target):
    answer = 0
    n_list = [0]
    for num in numbers :
        tmp = []
        for n in n_list:
            tmp.append(n + num)
            tmp.append(n - num)
        n_list = tmp
            
    return n_list.count(target)