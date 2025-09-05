import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))

# 1. 정렬
heights.sort()

# 2. 인접 차이 구하기
diffs = []
for i in range(1, n):
    diffs.append(heights[i] - heights[i-1])

# 3. 큰 차이부터 정렬
diffs.sort(reverse=True)

# 4. 가장 큰 (k-1)개 제거 → 나머지 합
answer = sum(diffs[k-1:])
print(answer)