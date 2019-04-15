## Pandas's Little Helpers
# do `import pandas as pd` because these require pandas
def drop_matching_rows(df, column, values):
    """
        Returns a dataframe excluding rows where a column value exists in the list of provided values
        This is kind of like a reverse .filter method
        Use this for when df.drop(['A', 'B']) throws "['A', 'B'] not found in axis"
    """
    return df[df[column].apply(lambda x:x not in values)]


# Come back to this, getting syntax errors...
# def compose(df, column, functions):
#     """
#         Returns a function composition, function piping of a list of functions chaining together .apply
#         Example compose(df, "towns", [get_before_paren, get_before_bracket]) becomes df["towns"].apply(get_before_paren).apply(get_before_bracket)

#     """
#     a = df.copy()
#     for f in functions:
#         a = df[df[column].apply(f)]

#     return a