from datetime import date, timedelta

def dates(start, count = None):
    try:
        if count==None:
            while(True):
                yield start
                start +=timedelta(days = 1)
                
        else: 
            for _ in range(count):
                yield start
                start = start + timedelta(days = 1)
    except StopIteration:
        return
    except OverflowError:
        return
generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
   print(next(generator))
except StopIteration:
    print('Error')