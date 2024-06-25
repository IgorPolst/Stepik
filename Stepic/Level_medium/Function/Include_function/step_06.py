password = [i for i in input()]
def condition (password):
    if any(map(lambda simbl: simbl.isdigit(), password)) and any(map(lambda simbl: simbl.isupper(), password)) and any(map(lambda simbl:simbl.islower(), password)):
        return True
    else:
        return False
print
if condition(password) and len(password) >= 7:
    print("YES")
else:
    print("NO")
