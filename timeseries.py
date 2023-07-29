import yfinance as yf
import pandas as pd
import requests

def SP500(save=False) -> yf.Ticker.history:
    """
    :param save: bool, default False
        If True, saves the data to data/sp500.csv
    :return: yf.Ticker.history
    """
    sp500 = yf.Ticker("^GSPC")
    sp500 = sp500.history(period="max")
    
    if save:
        sp500.to_csv("data/sp500.csv")

    return sp500[["Open", "High", "Low", "Close", "Volume"]]

def SP500Earnings(save=False) -> pd.DataFrame:
    URL="https://www.spglobal.com/spdji/en/documents/additional-material/sp-500-eps-est.xlsx"
    r = requests.get(URL)


    
    earnings_sheet = pd.read_excel(r.content, sheet_name="QUARTERLY DATA", skiprows=6, index_col=0)
    # Name index col
    earnings_sheet.index.name = "QUARTER END"
    names = ['OPERATING EARNINGS PER SHR', 'AS REPORTED EARNINGS SHR', 'CASH DIVIDENDS PER SHR', 'SALES PER SHARE', 'BOOK VAL PER SHARE', 'CAPITAL EXPENDITURE PER SHARE', 'PRICE', 'DIVISOR']

    earnings_sheet.columns = names


    if save:
        earnings_sheet.to_csv("data/sp500_earnings.csv")

    return earnings_sheet

# Run this file to update saved data
if __name__ == "__main__":
    SP500(save=True)
    SP500Earnings(save=True)

    


