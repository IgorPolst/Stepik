def translation(IP):
    IP_num = str(IP).split(".")[::-1]
    return sum(map(lambda part: int(part) * 256 ** IP_num.index(part), IP_num))


IP = [input() for _ in range(int(input()))]

print(*sorted(IP, key=translation), sep="\n")
