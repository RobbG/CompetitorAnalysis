import pandas as pd

Column_Names = ['City','ListAgentFirstName','ListAgentLastName','ListOfficeName','BuyerAgentFirstName',
                'BuyerAgentLastName','BuyerAgencyCompensation','BuyerOfficeName','OriginalListPrice',
                'ClosePrice','DaysOnMarket','CloseDate','ListingId','PropertySubType']

INPUT_FOLDER = 'D:\Competitor_Analysis\Pre_Loader\MLS.csv'
OUTPUT_FOLDER = 'D:\Competitor_Analysis\Done\Cleaned.csv'
def main():
    df = pd.read_csv(INPUT_FOLDER, usecols=Column_Names)
    df['ListAgentFirstName'] = df['ListAgentFirstName'].str.capitalize()
    df['ListAgentLastName'] = df['ListAgentLastName'].str.capitalize()
    df['ListOfficeName'] = df['ListOfficeName'].str.capitalize()
    df['ListOfficeName'] = df['ListOfficeName'].str.title()
    df['BuyerAgentFirstName'] = df['BuyerAgentFirstName'].str.capitalize()
    df['BuyerAgentLastName'] = df['BuyerAgentLastName'].str.capitalize()
    df['BuyerOfficeName'] = df['BuyerOfficeName'].str.title()
    df['CloseDate'] = pd.to_datetime(df['CloseDate']).dt.date

    df.to_csv(OUTPUT_FOLDER, index=False)









if __name__ == '__main__':
    main()