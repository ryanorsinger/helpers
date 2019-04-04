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
    return get_string_before_delimeter(x, "(")


def get_string_before_delimiter(string, delimiter):
    """
        Returns contents of a string before a given delimiter
        Example: get_string_before_delimiter("banana-kiwi", "-") returns "banana"
    """
    if delimiter in s:
        return (string[:string.index(delimiter)]).strip()
    else:
        return string