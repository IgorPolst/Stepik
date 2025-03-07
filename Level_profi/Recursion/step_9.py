def num_digit(num, count=0):
    if num == 0:
        print(count)
    else:
        count += 1
        num_digit(num//10, count)
        
    
num_digit(int(input()))