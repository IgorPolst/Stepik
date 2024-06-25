dict_scrable = {1:"AEILNORSTU", 2:"DG", 3:"BCMP", 4:"FHVWY", 5:"K", 8:"JX", 10:"QZ"}
val = 0
for i in input():
    for k,v in dict_scrable.items():
        if i in v:
            val += k
print(val)