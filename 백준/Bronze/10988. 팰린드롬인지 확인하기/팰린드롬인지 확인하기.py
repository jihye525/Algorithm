word = list(input())
rword = word[-1::-1]
chk = 1

for i in range(int(len(word)/2)+1):
    if word[i] != rword[i]:
        chk = 0
        break

print(chk)