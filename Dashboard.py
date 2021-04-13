import streamlit as st
import pandas as pd

def main():
    FOLDER = 'D:\\Competitor_Analysis\\Done\\Yucaipa_Q1_Cleaned.csv'
    df = pd.read_csv(FOLDER)

    transactions = df.count()[0]
    Ave_Days_On_Market = df['DaysOnMarket'].mean().round(decimals=0)
    Max_Days_On_Market = df['DaysOnMarket'].max().round(decimals=0)
    temp_closed = df['ClosePrice'].sum()
    total_dollars_closed = "${:,.2f}".format(temp_closed)

    print('Total dollars closed :',total_dollars_closed)
    print('Avenue days on market :', int(Ave_Days_On_Market))
    print('Max days on market :',int(Max_Days_On_Market))
    print('Number of transactions :', transactions)
if __name__ == '__main__':
    main()

