import sys

growth = [int(tall.strip("\n")) for tall in sys.stdin]
try:
    print(f"Рост самого низкого ученика: {min(growth)}")
    print(f"Рост самого высокого ученика: {max(growth)}")
    print(f"Средний рост: {sum(growth)//len(growth)}")
except:
    print("нет учеников")
