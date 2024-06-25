n = int(input())
first_element = 1
second_element = 1
for i in range(n):
    bufer = first_element + second_element
    print(first_element, end=" ")
    first_element = second_element
    second_element = bufer
