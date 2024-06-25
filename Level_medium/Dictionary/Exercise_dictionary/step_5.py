dict_country = {}
for _ in range(int(input())):
    country, *town = input().split()
    dict_country.setdefault(country, town)

for _ in range(int(input())):
    quest_town = input()
    for k, v in dict_country.items():
        if quest_town in v :
            print(k)
