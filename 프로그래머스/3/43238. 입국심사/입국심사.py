def solution(n, times):
    start = 0
    end = 1000000000*100000
    
#     while sum(end // t for t in times) < n:
#         start, end = end, end*2
        
        
    while start < end:
        mid = (start + end) // 2 
        person = sum(mid // t for t in times)
        
        if person < n:
            start = mid + 1
        else:
            end = mid 

    return start