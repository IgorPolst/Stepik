def print_products(*args):
    product_list = [i for i in args if type(i) is str and i!=""]
    if len(product_list) > 0:
        for i in range(len(product_list)):
                print(f"{i+1}) {product_list[i]}")
    else:
        print("Нет продуктов")

print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)