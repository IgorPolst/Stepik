def greet(name, *args):
    name = name.split()
    name.extend(list(args))
    hello = "Hello, " + " and ".join(name) + "!" 
    return hello
print(greet('Timur', 'Roman', 'Ruslan'))
