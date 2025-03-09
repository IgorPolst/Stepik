def remove_marks(text, marks):
    remove_marks.count += 1
    text = "".join(simbl for simbl in text if simbl not in marks)
    return text


remove_marks.count = int()
