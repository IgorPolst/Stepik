from operator import add, truediv, mul, sub
def arithmetic_operation (simbl):
    match simbl:
        case "*":
            return lambda a,b: a*b
        case "/":
            return lambda a,b: a/b
        case "+":
            return lambda a,b: a+b
        case "-":
            return lambda a,b: a-b
        