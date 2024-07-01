# 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
prime_lst = [True] * 1000001

m = int(1000001 ** 0.5)
for i in range(2, m + 1):
    if prime_lst[i]:           # i가 소수인 경우
        for j in range(i+i, 1000001, i): # i이후 i의 배수들을 False 판정
            prime_lst[j] = False


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, (n//2) + 1):
        if  prime_lst[i] and prime_lst[n-i]:
            cnt += 1

    print(cnt)