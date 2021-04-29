import streamlit as st
import pandas as pd

def main():
    FOLDER = 'D:\\Competitor_Analysis\\Done\\Yucaipa_Q1_Cleaned.csv'
    df = pd.read_csv(FOLDER)

    transactions = df.count()[0]
    ave_closed_sales_price = df['ClosePrice'].mean().round(decimals=0)
    ave_days_on_market = df['DaysOnMarket'].mean().round(decimals=0)
    max_days_on_market = df['DaysOnMarket'].max().round(decimals=0)
    min_days_on_market = df['DaysOnMarket'].min().round(decimals=0)
    temp_closed = df['ClosePrice'].sum()
    total_dollars_closed = "$ {:,.2f}".format(temp_closed)
    Broker_Listings = df['ListOfficeName'].value_counts()
    Property_Types = df['PropertySubType'].value_counts()
    buyer_agent_percentage = df['BuyerAgencyCompensation'].mean().round(decimals=0)
    buyer_agent_commission = df['Buyer Agent Commission'].round(decimals=0)

    st.sidebar.write('Sidebar area.')


    header = st.beta_container()
    with header:
        st.title('Competitive Analysis Quarter Based')
        st.write('Total transactions for 1st QTR', transactions)
        st.write('Avenue days on market', int(ave_days_on_market))
        st.write('Total Dollars Closed', total_dollars_closed)
        st.write('Max Days on Market', max_days_on_market)
        st.write('Min Days on Market', min_days_on_market)
        st.write('Ave Days on Market', int(ave_days_on_market))


if __name__ == '__main__':
    main()

