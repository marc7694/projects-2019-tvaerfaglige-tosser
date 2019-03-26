# DOWNLOAD STOCK DATA LINK https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=full&apikey=XU0S88ZM101LB0FQ&datatype=csv
###----- TEST PYTHON -----###
print("Så kører vi!") # Virker Python overhovedet?
###----- START KODE -----###
import pandas as pd

apikey = "XU0S88ZM101LB0FQ"
outputsize = "compact" # Compact or full. Compact is 100 points, full is 20+ years.

stocks_df = pd.DataFrame()
tickers = ["AAPL", "TSLA", "TEVA"]
print("\n-----------------------------------\n")
print("Based on individual dataframes:")
for ticker in tickers:
    fetch_link = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + ticker + "&outputsize=" + outputsize + "&apikey=" + apikey + "&datatype=csv"
    df = pd.read_csv(fetch_link)
    df["ticker"] = ticker
    print("Mean close for " + ticker +  " is " + str(round(df.close.mean(),2)))
    stocks_df = stocks_df.append(df,ignore_index=True)
print("\nBased on aggregate dataframe:")
print("Mean close for all stocks is " + str(round(stocks_df.close.mean(),2)))
print("\n-----------------------------------\n")
print(stocks_df)