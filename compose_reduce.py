def compose(*fns):
    from functools import reduce
    comp = lambda *fns: lambda x: reduce(lambda x,f: f(x), fns, x)
    return comp(*fns)

def remove_commas(s):
    return s.replace(',', '')


def remove_periods(s):
    return s.replace(".", "")


def remove_semicolons(s):
    return s.replace(";", "")

functions = [remove_semicolons, remove_periods, remove_commas]

# way of calling a variadic function to pass in a list.
# *functions unpacks the arguments
# composite1 = compose(*functions)

# composite2 = compose(remove_semicolons, remove_periods, remove_commas)

x = "1,2.3;4,,,,,,5;;;6;;;7.....8...9,.,.,.,.10"

composite_function = compose(*functions)

x = composite_function(x)
print(x)