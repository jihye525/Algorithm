t = int(input())

for _ in range(t):
    cnd, chd = map(int, input().split())
    print(f"You get {cnd//chd} piece(s) and your dad gets {cnd%chd} piece(s).")