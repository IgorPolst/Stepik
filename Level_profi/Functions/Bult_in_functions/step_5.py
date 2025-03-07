def is_greater(lists, number):
    return any(sum(lis) > number for lis in lists )
