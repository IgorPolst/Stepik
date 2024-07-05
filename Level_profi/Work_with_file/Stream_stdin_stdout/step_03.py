import sys

rounds = [int(round.strip("\n")) for round in sys.stdin]
if len(rounds)%2 == 1:
    if rounds[-1]%2 == 0:
        print("Анри")
    else:
        print("Дима")
else:
    if rounds[-1]%2 == 0:
        print("Дима")
    else:
        print("Анри")