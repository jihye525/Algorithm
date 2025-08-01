import bisect
import sys
input = sys.stdin.readline
problems = []
num_level_dict = {}

def add(num, level):
    bisect.insort_left(problems, (level, num))
    num_level_dict[num] = level

def get_recommend(x):
    if x == 1:
        return problems[-1][1]
    else:
        return problems[0][1]

def solved(p_num):
    level = num_level_dict.pop(p_num, None) # None을 안하면 keyError
    idx = bisect.bisect_left(problems, (level, p_num))
    if idx < len(problems) and problems[idx] == (level, p_num):
        problems.pop(idx)

def solve():
    n = int(input())

    for _ in range(n):
        p_num, level = map(int,input().split())
        add(p_num, level)

    m = int(input())
    for _ in range(m):
        oper = list(input().split())

        if oper[0] == "add":
            add(int(oper[1]), int(oper[2]))
        elif oper[0] == "solved":
            solved(int(oper[1]))
        elif oper[0] == "recommend":
            print(get_recommend(int(oper[1])))

solve()