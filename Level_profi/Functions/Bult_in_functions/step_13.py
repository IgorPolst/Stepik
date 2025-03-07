el = eval(input())

if isinstance(el, list):
    print(el[-1])
elif isinstance(el, tuple):
    print(el[0])
else:
    print(len(el))
