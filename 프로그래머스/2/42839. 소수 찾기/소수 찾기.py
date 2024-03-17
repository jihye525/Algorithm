from itertools import permutations

def solution(numbers):
    answer = 0
    numbers_list = [n for n in numbers]
    perm_list = []
    
    for i in range(1, len(numbers)+1):
        perm_list += permutations(numbers_list, i)
     
    num_set = set()
    for i in perm_list:
        num_set.add(int(''.join(i)))
        
    for n in num_set:
        if is_prime_num(n):
            answer += 1            
        
    return answer

def is_prime_num(n):
    factor = 0 

    for i in range(1, int(n / 2)+1):
        if n % i == 0:
            factor += 1
                
        
    if factor == 1:
        return True
    else:
        return False