import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def main():
    FOLDER = 'D:\Competitor_Analysis\Done\Yucaipa_Q1_Cleaned.csv'
    df = pd.read_csv(FOLDER)

    transactions = df.count()[0]
    ave_closed_sales_price = '$ {:,.2f}'.format(df['ClosePrice'].mean().round(decimals=0))
    ave_days_on_market = df['DaysOnMarket'].mean().round(decimals=0)
    max_days_on_market = df['DaysOnMarket'].max().round(decimals=0)
    min_days_on_market = df['DaysOnMarket'].min().round(decimals=0)
    total_dollars_closed = '$ {:,.2f}'.format(df['ClosePrice'].sum().round(decimals=0))
    broker_listings_totals = df['ListOfficeName'].value_counts()
    broker_listings = df.groupby(["ListOfficeName"])
    broker_listings = broker_listings["ClosePrice"].sum()


    property_types = df['PropertySubType'].value_counts()
    buyer_agent_ave_percentage = df['BuyerAgencyCompensation'].mean().round(decimals=0)
    total_buyer_agent_commissions = '$ {:,.2f}'.format(df['Buyer Agent Commission'].sum().round(decimals=0))



    st.sidebar.title('Make your select below')
    st.sidebar.selectbox(
        "Select Quarter",
        ("QTR-1", "QTR-2", "QTR-3", "QTR-4")
    )
    st.sidebar.selectbox(
        "Select City",
        ("Yucaipa", "Redlands")
    )

    st.title("Competitive Analysis")
    st.subheader("Quarterly Based")
    col1, col2 = st.beta_columns(2)
    with col1:
        fig = go.Figure(go.Indicator(
mode="number",
value=transactions,
title={
"text": "Total Transactions<br><span style='font-size:0.8em;color:black'></span>"},
domain={'x': [0, 1], 'y': [0, 1]}
))
    fig.update_layout(paper_bgcolor="lightblue")
    st.write(fig)

    with col2:
        fig1 = go.Figure(go.Indicator(
            mode="number",
            value=transactions,
            title={
                "text": "Total Transactions<br><span style='font-size:0.8em;color:pink'></span>"},
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
    fig1.update_layout(paper_bgcolor="lightblue")
    st.write(fig1)


    st.write('Total Dollars Closed', total_dollars_closed)
    st.write('Max Days on Market', max_days_on_market)
    st.write('Min Days on Market', min_days_on_market)
    st.write('Ave Days on Market', int(ave_days_on_market))
    st.write('Ave Closed Sales Price', ave_closed_sales_price)
    st.write('Ave Buyer Agent Commission', buyer_agent_ave_percentage)
    st.write('Total Buyer Agent Commission', total_buyer_agent_commissions)
    st.write('Broker Listings', broker_listings)
    st.write('Broker Total Listings', broker_listings_totals )



if __name__ == '__main__':
    main()

