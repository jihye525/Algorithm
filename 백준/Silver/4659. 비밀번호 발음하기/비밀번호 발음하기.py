import sys
input = sys.stdin.readline

def moum_check(s):
    for c in s:
        if c in {'a', 'e', 'i', 'o', 'u'}:
            return True
    return False

def two_serial_char(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s[i] not in {'e','o'}:
            return True
    return False

def three_serial_char(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(s)-2):
        if s[i] in vowels and s[i+1] in vowels and s[i+2] in vowels:
            return True
        if s[i] not in vowels and s[i+1] not in vowels and s[i+2] not in vowels:
            return True
    return False

def solve():
    while True:
        string = input().strip()
        if string == 'end':
            break

        if len(string) ==1 and moum_check(string):
            print(f"<{string}> is acceptable.")
        elif len(string) ==2 and moum_check(string) and not two_serial_char(string):
            print(f"<{string}> is acceptable.")
        elif len(string) >= 3 and moum_check(string) and not two_serial_char(string) and not three_serial_char(string):
            print(f"<{string}> is acceptable.")
        else:
            print(f"<{string}> is not acceptable.")


solve()