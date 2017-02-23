import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print "we're now in the decorator"
        func()
        print "This runs after the decorator func()"
    return function_that_runs_func

@my_decorator
def my_function():
    print ("I'm the func()")

#my_function()


# NB: Your decorator should always call the function (line 7)
#       else doesn't really matter what you're decorating :)

## MORE COMPLEX DECORATORS
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print "we're now in the decorator"
            if number == 56:
                print "not running the function"
            else:
                func(*args, **kwargs)
            print "This runs after the decorator func()"

        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(57)
def my_function_two(x, y):
    print x + y

my_function_two(200, 300)

## NB: Very useful for administrating accounts