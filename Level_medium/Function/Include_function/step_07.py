great_class = []
def find_great_student (studentes):
    return any(map(lambda stud: stud[1] == "5", studentes))
    
for _ in range(int(input())):
    studentes = [tuple(input().split()) for _ in range(int(input()))]
    great_class.append(find_great_student(studentes))


if all(great_class):
    print("YES")
else:
    print("NO")
