def output_decorator(title):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            print("#########################")
            print("# " + title)
            print("# input: " + ", ".join(str(x) for x in args))
            print("# output: " + str(result))
            print("#########################")
            print()
            return result
        return wrapper
    return decorator
@output_decorator("Adding")
def add(a, b):
    return a + b

add(4, 3)