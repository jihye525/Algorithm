def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    
    if isPrime(yellow):
        return [yellow + 2, 3]
    
    for i in range(2, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            width = (yellow / i) + 2
            height = i + 2
            if width - 1 + height - 1 == brown / 2 :
                return [width, height]           

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True