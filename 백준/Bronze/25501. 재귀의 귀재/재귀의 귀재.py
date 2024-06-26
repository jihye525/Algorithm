def recursion(s, l, r, func_call_num):
    if l >= r: 
        print(1, func_call_num)
        return
    elif s[l] != s[r]: 
        print(0, func_call_num)
        return
    else: 
        return recursion(s, l+1, r-1, func_call_num + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

n = int(input())
for _ in range(n):
    isPalindrome(input())
