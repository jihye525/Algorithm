n = int(input())
temp = list(map(int, input().split()))
dic = dict().fromkeys(temp, 1)

m = int(input())
lst = list(map(int, input().split()))

for i in lst:
    print(1 if dic.get(i) else 0, end=" ")