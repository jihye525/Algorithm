from collections import Counter

def solution(a):
    answer = 0 
    sub_set = Counter(a)
    cnt = 0
    left = 0
    for k in sub_set.keys():
        if sub_set[k] <= answer:
            continue
        idx = 0
        cnt = 0
        while idx < len(a)-1:
            if (a[idx]!= k and a[idx+1]!= k) or a[idx] == a[idx+1]:
                idx+=1
                continue
            cnt+=1
            idx+=2
        answer= max(answer,cnt)
        
    return answer*2