from collections import ChainMap

fruits = ChainMap(
    {"apple": 10, "banana": 20}, {"lemon": 10, "pineapple": 15}, {"kiwi": 15, "lime": 5}
)

print(*fruits.keys())
fruits = ChainMap(
    {"kiwi": 10, "banana": 20}, {"lime": 10, "pineapple": 15}, {"kiwi": 15, "lime": 5}
)

print(*fruits)

fruits = ChainMap(
    {"kiwi": 10, "banana": 20}, {"lime": 10, "pineapple": 15}, {"kiwi": 15, "lime": 5}
)

print(*fruits.items())
