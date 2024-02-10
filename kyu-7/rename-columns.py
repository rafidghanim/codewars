import pandas as pd

def rename_columns(df, names):  
    return df.set_axis(names, axis='columns', copy=False)
