a, b, c = int(input()), int(input()), int(input())

if a == b and b == c and a == c:
    print("Равносторонний")
elif a != b and a != c and b != c:
    print("Разносторонний")
else:
    print("Равнобедренный")
