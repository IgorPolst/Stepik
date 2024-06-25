town = set([input() for _ in range (int (input()))])
new_town = set(input())

if town&new_town != set():
    print("REPEAT")
else:
    print("OK")