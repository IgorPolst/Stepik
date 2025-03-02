from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    sorted_dict = OrderedDict()
    
    if(by_values):
        sorted_dict = sorted(ordered_dict.items(), key = lambda d: d[1]) 
    else:
        sorted_dict = sorted(ordered_dict.items(), key = lambda d: d[0])
        
    for key in sorted_dict:
            ordered_dict.move_to_end(key[0]) 
       

data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())