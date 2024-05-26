n = int(input())
vote = input()

a_cnt = vote.count('A')
b_cnt = vote.count('B')

if a_cnt == b_cnt:
    print("Tie")
elif a_cnt > b_cnt:
    print("A")
else:
    print("B")