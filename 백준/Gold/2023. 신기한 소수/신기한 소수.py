import sys
input = sys.stdin.readline
N = int(input())

def isPrime(num): 
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True
    
    
def DFS(number):
    if len(str(number)) == N:
        print(number)
        return
    for i in range(1, 10):
        if i % 2 == 0: # 짝수는 넘김
            continue
        elif isPrime(number * 10 + i): 
            DFS(number * 10 + i) 
    
    
#맨 앞자리는 일의 자리 소수인 2,3,5,7만 올 수 있음
DFS(2)
DFS(3)
DFS(5)
DFS(7)