def solution(n, times):
    answer = 0
    start = 0
    end = 1
    
    while sum(end // t for t in times) < n:
        start, end = end, end*2
        
        
    while start < end:
        mid = (start + end) // 2 
        person = sum(mid // t for t in times)
        
        if person < n:
            start = mid + 1
        else:
            end = mid 


    return start