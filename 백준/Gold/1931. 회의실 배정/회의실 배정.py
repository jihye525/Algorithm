import sys
input = sys.stdin.readline

n = int(input())
reservations = [list(map(int, input().split())) for _ in range(n)]
reservations.sort(key=lambda r: (r[1], r[0]))  # 끝나는 시간 기준 정렬

answer = 0
last_end = 0  # 마지막으로 선택한 회의의 끝나는 시간

for start, end in reservations:
    if start >= last_end:  # 겹치지 않으면 선택
        answer += 1
        last_end = end

print(answer)