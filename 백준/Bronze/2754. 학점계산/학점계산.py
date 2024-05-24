grade = input()
score = 0.0
for c in grade:
    if c == 'A':
        score += 4.0
    if c == 'B':
        score += 3.0
    if c == 'C':
        score += 2.0
    if c == 'D':
        score += 1.0
    if c == '+':
        score += 0.3
    if c == '-':
        score -= 0.3

print(score)