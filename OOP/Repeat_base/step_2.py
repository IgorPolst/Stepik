balance = 0
for char in input():
    if char == '(': balance += 1
    elif char == ')':
        balance -= 1
        if balance < 0: break

print(balance == 0)