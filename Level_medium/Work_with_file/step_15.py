n = int(input())
for _ in range(n):
    with open(f"{input().strip()}", "rt") as read_file, open("output.txt", "at" ) as res:
        lines = read_file.readlines()
        for line in lines:
            res.write(line)