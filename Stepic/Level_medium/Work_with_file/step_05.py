with open("Work_with_file/num.txt", "rt") as file:
    data = file.read()
    print(type(data)) 
    for i in range(len(data)):
        print(data[i])
        if data[i] not in "0123456789":
            data = data.replace(data[i], " ")
            print(data)
    numbers = [int(i.strip()) for i in data.split()]
    print(sum(numbers))
