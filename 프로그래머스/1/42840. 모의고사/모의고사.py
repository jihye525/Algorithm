def solution(answers):
    answer = [0,0,0]
    list2 = [2,1,2,3,2,4,2,5]
    list3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    for i in range(len(answers)):
        if answers[i] == (int)(i % 5) + 1 :
            answer[0] += 1
            
        if answers[i] == list2[i % 8]:
            answer[1] += 1
        
        if answers[i] == list3[i % 10]:
            answer[2] += 1
            
    
    return [(i + 1) for i, value in enumerate(answer) if value == max(answer)]