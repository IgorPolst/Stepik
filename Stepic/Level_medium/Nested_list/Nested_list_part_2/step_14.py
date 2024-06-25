input_data = input().split()
output_data = [[]]
for i in range(len(input_data)):
    for j in range(len(input_data) - i):
        output_data.append(input_data[j: j + i + 1])
print(output_data)