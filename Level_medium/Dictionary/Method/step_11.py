text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
keys = set(text)
value = [text.count(i) for i in sorted(keys)]
result = dict(zip(sorted(keys), value))
print(result)