athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def names(name):
    return name[creteriy]

def ages(age):
    return age[creteriy]

def heightes(height):
    return height[creteriy]

def weightes(weight):
    return weight[creteriy]

function_list = [names, ages, heightes, weightes]
creteriy = int(input())-1
for i in sorted(athletes, key = function_list[creteriy]):
    print (*i)