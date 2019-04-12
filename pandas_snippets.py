
# dataframe has state names and towns in the towns           
#           towns
# 0       Alabama
# 1        Auburn
# 2      Florence
# 3  Jacksonville
# 4    Livingston


# return the data frame with all of the rows removed that exist in a list
new_df = df[df["towns"].apply(lambda x:x not in state_names)]

# or
mask = df["towns"].apply(lambda x:x not in state_names)
new_df = df[mask]


def drop_rows(df, column, values):
    """
        Returns a dataframe excluding rows where a column value exists in the list of provided values
        Use this for when df.drop(['A', 'B']) throws "['A', 'B'] not found in axis"
    """
    return df[df[column].apply(x:x not in values)]