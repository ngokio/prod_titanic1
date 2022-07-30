import pandas as pd
'''return the first letter of serie in a dataframe'''
def first_letter(serie):
  return pd.DataFrame(serie.str[0])