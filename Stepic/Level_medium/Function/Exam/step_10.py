def compose (fun, gun):
    return lambda x: fun(gun(x)) 