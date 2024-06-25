town1, town2, town3 = str(input()), str(input()), str(input())

cost_town1 = len(town1)
cost_town2 = len(town2)
cost_town3 = len(town3)

if min(cost_town1, cost_town2, cost_town3) == cost_town1:
    print(town1)
elif min(cost_town1, cost_town2, cost_town3) == cost_town2:
    print(town2)
else:
    print(town3)

if max(cost_town1, cost_town2, cost_town3) == cost_town1:
    print(town1)
elif max(cost_town1, cost_town2, cost_town3) == cost_town2:
    print(town2)
else:
    print(town3)
