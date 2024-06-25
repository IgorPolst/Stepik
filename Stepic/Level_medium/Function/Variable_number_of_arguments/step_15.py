def info_kwargs(**kwargs):
    for key, val in sorted(kwargs.items()):
        print (f"{key}: {val}")
info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')