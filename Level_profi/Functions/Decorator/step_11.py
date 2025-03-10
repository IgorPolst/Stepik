import functools


def make_html(tag):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)

            return f"<{tag}>{res}</{tag}>"

        return wrapper

    return decorator

@make_html('del')
def get_text(text):
    return text
    
print(get_text('Python'))

@make_html('i')
@make_html('del')
def get_text(text):
    return text
    
print(get_text(text='decorators are so cool!'))