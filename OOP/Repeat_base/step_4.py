import sys

lines = [card for card in sys.stdin]
collections = {card: lines.count(card) for card in lines}
print(sum(map(lambda el: el-1, collections.values())))