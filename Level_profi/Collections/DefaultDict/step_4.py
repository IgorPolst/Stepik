from collections import defaultdict

def wins(pairs):
    winer = defaultdict(set)
    for round in pairs:
        winer[round[0]].add(round[1])
    return winer

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))