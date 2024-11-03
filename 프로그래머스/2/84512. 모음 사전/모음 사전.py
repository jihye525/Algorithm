ans = 0
num = 0
def dfs(current_word, n, target):
    global ans, num
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    if n == 5:
        return

    for c in alpha:
        num += 1
        if current_word + c == target:
            ans = num
        dfs(current_word + c, n + 1, target)
        
def solution(word):
    dfs('', 0, word)
    return ans
