def remove_digits(s):
    """
        Returns a string with all digits removed.
    """
    return ''.join(filter(lambda x: not x.isdigit(), s))


def remove_parentheticals(x):
    """
        Removes any parenthetical expression from a string
        Returns "Bolivia" from "Bolivia (Plurinational State of)" 
    """ 
    if "(" in x:
        return (x[:x.index("(")]).strip()
    else:
        return x
