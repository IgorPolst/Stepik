def build_query_string(params):
    list_quest = []
    for i in params:
        list_quest.append(i+"="+str(params[i]))    
    return ("&".join(sorted(list_quest)))


print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))