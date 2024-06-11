t = int(input())
cnt = 0
for _ in range(t):
    word = input()
    visited = [0] * 26
    not_continued = 0
    for i in range(len(word)):
        idx = ord(word[i]) - 97
        if not visited[idx]:  # 처음 나온 문자는 체크
            visited[idx] = i + 1
        else:
            if visited[idx] == i: #이미 나온 문자이지만 연속되었을 때
                visited[idx] = i + 1  #연속된 인덱스 중 마지막 값으로 갱신
            else: # 이미 나온 문자이고 연속되지 않았을 때
                not_continued = 1
                break

    if not_continued:
        continue

    cnt += 1

print(cnt)