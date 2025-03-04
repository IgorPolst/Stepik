from collections import Counter, ChainMap


bread = {"булочка с кунжутом": 15, "обычная булочка": 10, "ржаная булочка": 15}
meat = {"куриный бифштекс": 50, "говяжий бифштекс": 70, "рыбный бифштекс": 40}
sauce = {
    "сливочно-чесночный": 15,
    "кетчуп": 10,
    "горчица": 10,
    "барбекю": 15,
    "чили": 15,
}
vegetables = {"лук": 10, "салат": 15, "помидор": 15, "огурцы": 10}
toppings = {"сыр": 25, "яйцо": 15, "бекон": 30}

ingridients = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(sorted(input().split(",")))

max_len = len(max(order.keys(), key=lambda el: len(el)))
total = 0
result = str()
for name, count in order.items():
    total += ingridients[name] * count
    result = name.ljust(max_len) + f" x {count}"
    print(result)

total = f"ИТОГ: {total}р"

total_result = len(total)
print(len(result) * "-" if len(result) > total_result else total_result * "-")
print(total)
