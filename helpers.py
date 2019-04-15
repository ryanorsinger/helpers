def remove_digits(s):
    """
        Returns a string with all digits removed.
    """
    return ''.join(filter(lambda x: not x.isdigit(), s))


def remove_parentheticals(s):
    """
        Removes any parenthetical expression from a string
        Returns "Bolivia" from "Bolivia (Plurinational State of)" 
    """ 
    return get_string_before_delimeter(s, "(")


def get_string_before_delimiter(string, delimiter):
    """
        Returns contents of a string before a given delimiter
        Example: get_string_before_delimiter("banana-kiwi", "-") returns "banana"
    """
    if delimiter in string:
        return (string[:string.index(delimiter)]).strip()
    else:
        return string

def get_after_delimiter(string, delimiter):
    """
        Returns the string contents after the first occurance of the provided delimiter
        Example: get_after_delimiter("This, that, and the other", ",") returns "that, and the other"
    """
    if string in delimiter:
        return string[string.index(delimiter) + 1:].strip()
    else:
        return string

def get_after_comma(s):
    """
        Returns the string contents after the first comma
        Example: get_after_comma("This, that, and the other") returns "that, and the other"
    """
    return get_after_delimiter(s, ",")


## Pandas's Little Helpers
# do `import pandas as pd` because these require pandas
def drop_matching_rows(df, column, values):
    """
        Returns a dataframe excluding rows where a column value exists in the list of provided values
        This is kind of like a reverse .filter method
        Use this for when df.drop(['A', 'B']) throws "['A', 'B'] not found in axis"
    """
    return df[df[column].apply(lambda x:x not in values)]