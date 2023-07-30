import pandas as pd
import datetime as dt

def dateMatcher(small: pd.DataFrame, big: pd.DataFrame, col1=None, col2=None) -> pd.DataFrame:
    # Assuming that all elements of small are in big 
    if col1 is None:
        col1 = small.index

    if col2 is None:
        col2 = big.index

    # Convert to datetime
    small[col1] = pd.to_datetime(small[col1])
    big[col2] = pd.to_datetime(big[col2])

    combined = pd.merge_asof(small, big, left_on=col1, right_on=col2, direction="nearest")



    

    



    
    
   