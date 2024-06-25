number = input()

number = number[::-1]
new_number = ""

count = 0
for i in range(len(number)):
    if count == 3:
        new_number += "," + number[i]
        count = 1
    else:
        new_number += number[i]
        count += 1
print(new_number[::-1])
