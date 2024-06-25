question = {int (i) for i in input().split() }
answer = {int (i) for i in input().split() }

if question.issubset(answer) and len(question) == len(answer):
    print("YES")
else:
    print("NO")