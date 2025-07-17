from itertools import combinations
import sys

def calculate_distance(shops, houses):
    global min_distance
    distance = [sys.maxsize] * len(houses)
    for s in shops:
        for i in range(len(houses)):
            d = abs(s[0] - houses[i][0]) + abs(s[1] - houses[i][1])
            distance[i] = min(distance[i], d)
    min_distance = min(min_distance, sum(distance))

def solve():
    for i in combinations(chicken_shop, m):
        calculate_distance(i, houses)

input = sys.stdin.readline
n, m = map(int, input().split())
city = list()
houses = list()
chicken_shop = list()
min_distance = sys.maxsize

for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(len(city[i])):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chicken_shop.append([i, j])

solve()
print(min_distance)