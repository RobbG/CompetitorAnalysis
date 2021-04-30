import pandas as pd

Column_Names = ['City','ListAgentFirstName','ListAgentLastName','ListOfficeName','BuyerAgentFirstName',
                'BuyerAgentLastName','BuyerAgencyCompensation','BuyerOfficeName','OriginalListPrice',
                'ClosePrice','DaysOnMarket','CloseDate','ListingId','PropertySubType']

QTR =""
INPUT_FOLDER = 'D:\Competitor_Analysis\Pre_Loader\Yucaipa_Q1.csv'
OUTPUT_FOLDER = 'D:\Competitor_Analysis\Done\Yucaipa_Q1_Cleaned.csv'
def main():
    df = pd.read_csv(INPUT_FOLDER, usecols=Column_Names)

    df['ListAgentFirstName'] = df['ListAgentFirstName'].str.lower()
    df['ListAgentLastName'] = df['ListAgentLastName'].str.lower()
    df["Listing Agent Name"] = df["ListAgentFirstName"].str.cat(df["ListAgentLastName"], sep=" ")
    df = df.drop(["ListAgentFirstName", "ListAgentLastName"], axis=1)
    df['ListOfficeName'] = df['ListOfficeName'].str.lower()
    df['ListOfficeName'] = df['ListOfficeName'].str.lower()
    df['BuyerAgentFirstName'] = df['BuyerAgentFirstName'].str.lower()
    df['BuyerAgentLastName'] = df['BuyerAgentLastName'].str.lower()
    df["Buyer Agent Name"] = df["BuyerAgentFirstName"].str.cat(df["BuyerAgentLastName"], sep=" ")
    df = df.drop(["BuyerAgentFirstName", "BuyerAgentLastName"], axis=1)
    df['BuyerOfficeName'] = df['BuyerOfficeName'].str.lower()
    df['Month'] = pd.DatetimeIndex(df['CloseDate']).month
    df['Year'] = pd.DatetimeIndex(df['CloseDate']).year
    df = df.drop(["CloseDate"], axis=1)
    df['Buyer Agent Commission'] = df['ClosePrice'] * df['BuyerAgencyCompensation']/100
    df['Buyer Agent Commission'] = df['Buyer Agent Commission'].astype(int)
    df.to_csv(OUTPUT_FOLDER, index=False)

if __name__ == '__main__':
    main()