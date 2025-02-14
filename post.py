import pandas as pd
import json

# Load the CSV data

dfs=[
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ADANIPORTS.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ASIANPAINT.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/AXISBANK.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/BAJAJ-AUTO.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/BAJFINANCE.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/BAJAJFINSV.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/BHARTIARTL.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/INFRATEL.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/BRITANNIA.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/CIPLA.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/COALINDIA.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/DRREDDY.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/EICHERMOT.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/GAIL.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/GRASIM.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HCLTECH.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HDFC.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HDFCBANK.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HEROMOTOCO.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HINDALCO.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/HINDUNILVR.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ICICIBANK.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/INDUSINDBK.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/INFY.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/IOC.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ITC.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/JSWSTEEL.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/KOTAKBANK.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/LT.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/MM.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/MARUTI.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/NESTLEIND.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/NTPC.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ONGC.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/POWERGRID.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/RELIANCE.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/SBIN.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/SHREECEM.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/SUNPHARMA.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/TATAMOTORS.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/TATASTEEL.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/TCS.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/TECHM.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/TITAN.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ULTRACEMCO.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/UPL.csv')    ,
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/WIPRO.csv'),
    pd.read_csv('/home/lopamudra/Documents/WiDS-2024/DATA/ZEEL.csv')
]

#dfss be list of all the file present in DATA folder

#Date,Symbol,Series,Prev Close,Open,High,Low,Last,Close,VWAP,Volume,Turnover,Trades,Deliverable Volume,%Deliverble


# Function to create questions and answers for all columns
def create_qa_pairs(dfs):
    qa_pairs = []
    for df in dfs:
        for index, row in df.iterrows():
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}",
                "question": f"What was the closing price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Close'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}a",
                "question": f"What was the volume of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Volume'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}b",
                "question": f"What was the highest price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['High'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}c",
                "question": f"What was the lowest price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Low'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}d",
                "question": f"What was the opening price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Open'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}e",
                "question": f"What was the previous closing price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Prev Close'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}f",
                "question": f"What was the last traded price of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Last'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}g",
                "question": f"What was the VWAP of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['VWAP'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}h",
                "question": f"What was the turnover of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Turnover'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}i",
                "question": f"What was the number of trades of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Trades'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}j",
                "question": f"What was the deliverable volume of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['Deliverable Volume'])]
            })
            qa_pairs.append({
                "id": f"{row['Symbol']}_{index + 1}k",
                "question": f"What was the percentage deliverable of {row['Symbol']} on {row['Date']}?",
                "answers": [str(row['%Deliverble'])]
            })
    return qa_pairs

# Create question-answer pairs
qa_pairs = create_qa_pairs(dfs)

# Save the question-answer pairs to a JSON file
with open('/home/lopamudra/Documents/WiDS-2024/stock_market_qa.json', 'w') as f:
    json.dump(qa_pairs, f, indent=4)

print("Data saved to stock_market_qa.json")