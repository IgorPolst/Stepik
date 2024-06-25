from decimal import *

num = Decimal(input())

digits_list = [int(i) for i in num.as_tuple().digits]
if int(num) == 0:
    print(max(digits_list))
else:
    print(max(digits_list) + min(digits_list))
