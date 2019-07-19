
# reassign the dataframe to be the result of the following .loc
# .loc[start_row:end_row, start_column:end_column]
# .loc[:, "Under 5":"18 years"] will return all columns between and including

df["age_bin_0-19"] = df.loc[:, 'Estimate Male Under 5':'Estimate Male 18']


df = DataFrame(np.random.rand(4,5), columns = list('abcde'))

df.loc[:, "b":"d"] # returns the b, c, and d columns
