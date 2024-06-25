color1, color2 = str(input()), str(input())

if (
    color1 == "синий"
    and color2 == "красный"
    or color1 == "красный"
    and color2 == "синий"
):
    print("фиолетовый")
elif (
    color1 == "синий" and color2 == "желтый" or color1 == "желтый" and color2 == "синий"
):
    print("зеленый")
elif (
    color1 == "красный"
    and color2 == "желтый"
    or color1 == "желтый"
    and color2 == "красный"
):
    print("оранжевый")
elif color1 == color2 and color2 == "желтый":
    print("желтый")
elif color1 == color2 and color2 == "красный":
    print("красный")
elif color1 == color2 and color2 == "синий":
    print("синий")
else:
    print("ошибка цвета")
