n = int(input())
score = 0
for _ in range(n):
    score += int(input())

if score > int(n/2):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")