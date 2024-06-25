first, second, third = int(input()), int(input()), int(input())

if second <= first <= third or second >= first >= third:
    bufer = first
elif first <= second <= third or first >= second >= third:
    bufer = second
else:
    bufer = third

print(max(first, second, third))
print(bufer)
print(min(first, second, third))
