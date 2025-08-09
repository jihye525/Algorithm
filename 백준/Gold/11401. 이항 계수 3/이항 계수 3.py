import sys
input = sys.stdin.readline

MOD = 10**9 + 7

n, k = map(int, input().split())

# 팩토리얼 계산
fact = [1] * (n+1)
for i in range(2, n+1):
    fact[i] = fact[i-1] * i % MOD

# 페르마 소정리를 이용한 모듈러 역원 계산 (pow 함수 사용) 페르마 소정리 -> b^-1 = b^(M-2) mod M
inv_fact = [1] * (n+1)
inv_fact[n] = pow(fact[n], MOD-2, MOD) # pow(2, 10, 1000) -> (2^10)1024 % 1000 = 24
for i in range(n-1, 0, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

# 조합 함수
def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

print(comb(n, k))
