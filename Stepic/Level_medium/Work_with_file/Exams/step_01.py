with open("Exams\grades.txt", "rt") as file: 
    data = file.readlines()

check = lambda score: score >= 65 
count = 0
for line in data:
    student = line.strip().split()
    balls = []
    for ball in range(1, 4):
        balls.append(check(int(student[ball])))
    if all(balls):
        count+=1
print(count)
