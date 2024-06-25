from random import randrange
def generate_ip():
    n = ".".join([str(randrange(255)) for _ in range (4)])
    return n

print(generate_ip())