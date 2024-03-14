def solution(tickets):
    route = []
    visited = [False] * len(tickets)
    
    def dfs(airport, path):
        
        if len(path) == len(tickets) + 1:
            route.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if not visited[idx] and ticket[0] == airport:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
    
    dfs("ICN",["ICN"])
    
    route.sort()
    
    return route[0]
