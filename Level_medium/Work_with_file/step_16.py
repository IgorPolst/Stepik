def translater(time):
    hour, minutes = time.split(":")
    return int(hour) * 60 + int(minutes)


def time_counter(start, finish):
    return translater(finish) - translater(start) >= 60

with open("Work_with_file/logfile.txt", "rt", encoding="utf-8") as data, open("output.txt", "wt") as out:
    name = []
    for line in data: 
        informat = line.strip().split(", ")
        if time_counter(informat[1],informat[2]):
            out.write(informat[0]) 

