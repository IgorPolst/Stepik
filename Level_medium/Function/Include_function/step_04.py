# IP-адрес – уникальный числовой идентификатор устройства в компьютерной сети, работающей по протоколу TCP/IP.

# В 4-й версии IP-адрес представляет собой 32-битное число. 
# Адрес записывается в виде четырёх десятичных чисел (октетов) 
# со значением от 0 до 255 (включительно), разделённых точками, 
# например, 192.168.1.2

# Напишите программу с использованием встроенной функции 
# all() для проверки корректности IP-адреса: 
# все ли октеты в IP-адресе – числа со значением от 0 до 255.

IP = [i for i in input().split(".")]
print(all(map(lambda num: num.isdigit() and 0<= int(num) <= 255, IP))) 