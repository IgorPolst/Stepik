import pickle
import sys

with open(input(), "rb") as file:
    lonly_function = pickle.load(file)

print(lonly_function(*list(map(str.strip, sys.stdin))))