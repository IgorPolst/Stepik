def annual_return(start, percent, years):
    for _ in range(years):
        start *= ((percent + 100)/100)
        yield start

for value in annual_return(120000, 10, 3):
    print(round(value))