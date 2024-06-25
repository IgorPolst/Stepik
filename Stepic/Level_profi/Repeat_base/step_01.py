def hide_card(bad_number):
    number_list = bad_number.split()
    if len(number_list) > 1:
        number_list = "".join(number_list)
    else:
        number_list = number_list[0]
    print(number_list)
    return "*" * 12 + number_list[-4:]


print(hide_card("905 678123 45612 56"))

# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]