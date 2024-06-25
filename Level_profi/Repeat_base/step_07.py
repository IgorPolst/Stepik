def likes(names):
    length = len (names)
    match length:
        case 0: 
            return "Никто не оценил данную запись"
        case 1: 
            return f"{names[0]} оценил(а) данную запись"
        case 2: 
            return f"{names[0]} и {names[1]} оценили данную запись"
        case 3:
            return f"{names[0]}, {names[1]} и {names[2]} оценили данную запись"
        case _:
            return f"{names[0]}, {names[1]} и {length-2} других оценили данную запись"

print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))