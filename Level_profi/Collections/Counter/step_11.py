from collections import Counter


data = Counter(
    "aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi"
)
data.min_values = lambda: list(
    filter(lambda el: el[1] == min(data.values()), data.items())
)
data.max_values = lambda: list(
    filter(lambda el: el[1] == max(data.values()), data.items())
)
print(data.min_values)
