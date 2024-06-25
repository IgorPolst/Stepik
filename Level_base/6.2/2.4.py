# Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.
a = int(input())
print(a)
print(a + 1)
print(a + 2)

# Программа должна вывести сумму введенных чисел
e = int(input())
b = int(input())
c = int(input())
print(e + b + c)

# Программа должна вывести текст и числа в соответствии с условием задачи
f = int(input())
print("Объем =", f * f * f)
print("Площадь полной поверхности =", 6 * f * f)


first = int(input())
second = int(input())
function = (
    3 * (first + second) * (first + second) * (first + second)
    + 275 * second * second
    - 127 * first
    - 41
)
print(function)

# Программа должна вывести текст согласно условию задачи
number = int(input())
print("Следующее за числом", number, "число:", number + 1)
print("Для числа", number, "предыдущее число:", number - 1)

# Программа должна вывести одно число – стоимость покупки (трех компьютеров).
cost_monitor = int(input())
cost_system = int(input())
cost_keyboard = int(input())
cost_mice = int(input())
print(3*(cost_keyboard + cost_mice + cost_monitor + cost_system))

#Программа должна вывести сумму, разность и произведение введённых чисел, каждое на отдельной строке.

fir = int(input())
sec = int(input())
print(fir, "+", sec, "=", fir+sec)
print(fir, "-", sec, "=", fir-sec)
print(fir, "*", sec, "=", fir*sec)

#Программа должна вывести n-ый член арифметической прогрессии.

a1 = int(input())
d_a1 = int(input())
n = int(input())
print(a1+d_a1*(n-1))

#Программа должна вывести текст согласно условию задачи.
x = int(input())
print(x, 2*x, 3*x, 4*x, 5*x, sep="---")