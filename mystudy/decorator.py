from functools import wraps

def add_wrapping_with_style(style):
    def add_wrapping(item):
        @wraps(item)
        def wrapped_item():
            result = item()
            return "a {} wrapped up box of {}".format(style, str(result))
        return wrapped_item
    return add_wrapping

def add_wrapping(item):
    @wraps(item)
    def wrapped_item():
        result = item()
        return "a wrapped up box of {}".format(str(result))
    return wrapped_item

@add_wrapping
def new_gpu():
    return "a new Tesla 100 GPU"

@add_wrapping_with_style("beautifully")
def new_bicycle():
    return "a new bicycle"

print(new_gpu())
print(new_bicycle())

# print(new_gpu.__name__)

