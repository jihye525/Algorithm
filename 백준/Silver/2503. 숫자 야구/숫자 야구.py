import sys
sys.setrecursionlimit(999999999)
input = sys.stdin.readline

def checker(idx, number):
    q_number, strike, ball = hint[idx]
    s, b = 0, 0
    A = q_number % 10
    B = q_number // 10 % 10
    C = q_number // 100 % 10

    _A = number % 10
    _B = number // 10 % 10
    _C = number // 100 % 10

    if _A == _B or _A == _C or _B == _C:
        return False

    if _A == 0 or _B == 0 or _C == 0:
        return False

    if _A == A:
        s += 1
    if _B == B:
        s += 1
    if _C == C:
        s += 1

    if _A == B or _A == C:
        b += 1
    if _B == A or _B == C:
        b += 1
    if _C == A or _C == B:
        b += 1

    if strike == s and ball == b:
        return True

    return False


#123 ~ 987 모든 숫자
def recur(hint_idx, number):
    global answer
    # 모든 힌트와 일치한다면 답 +1 and 다음 숫자
    if hint_idx == n:
        answer += 1
        recur(0, number + 1)
        return
    if number == 988:
        return

    # 힌트와 일치한다면
    if checker(hint_idx, number):
        recur(hint_idx + 1, number)
    else: # 힌트와 일치하지 않는다면
        recur(0, number + 1)


n = int(input())
hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0
recur(0, 123)
print(answer)