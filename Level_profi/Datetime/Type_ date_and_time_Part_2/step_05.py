from datetime import date

dates = sorted([input() for _ in range(int(input()))])

print(*map(lambda dat: date.fromisoformat(dat).strftime("%d/%m/%Y"), dates), sep="\n")
