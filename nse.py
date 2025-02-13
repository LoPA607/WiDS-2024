import requests
import pandas as pd
import time

class NseIndia:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)

    def get_stock_info(self, symbol):
        base_url = 'https://www.nseindia.com/api/quote-equity?symbol=' + symbol.replace(' ', '%20').replace('&', '%26')
        url1 = f"{base_url}&section=trade_info"
        url2 = f"{base_url}"

        response1 = self.session.get(url1, headers=self.headers).json()
        response2 = self.session.get(url2, headers=self.headers).json()
        
        # Extract trade and price info
        tc = response1.get('marketDeptOrderBook', {}).get('tradeInfo', {}).get('totalMarketCap', 'None')
        fc = response1.get('marketDeptOrderBook', {}).get('tradeInfo', {}).get('ffmc', 'None')
        lp = response2.get('priceInfo', {}).get('lastPrice', 'None')
        day_high = response2.get('priceInfo', {}).get('intraDayHighLow', {}).get('max', 'None')
        day_low = response2.get('priceInfo', {}).get('intraDayHighLow', {}).get('min', 'None')
        wk52_high = response2.get('priceInfo', {}).get('weekHighLow', {}).get('max', 'None')
        wk52_low = response2.get('priceInfo', {}).get('weekHighLow', {}).get('min', 'None')
        volume = response2.get('priceInfo', {}).get('totalTradedVolume', 'None')
        change_perc = response2.get('priceInfo', {}).get('change', 'None')
        
        # Industry info
        ma = response2.get("industryInfo", {}).get("macro", 'None')
        se = response2.get("industryInfo", {}).get("sector", 'None')
        ind = response2.get("industryInfo", {}).get("industry", 'None')
        bas = response2.get("industryInfo", {}).get("basicIndustry", 'None')
        
        return (tc, fc, lp, day_high, day_low, wk52_high, wk52_low, volume, change_perc, ma, se, ind, bas)


# List of top companies
top_companies = list(set([
    'RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'HDFC', 'ITC', 'ICICIBANK', 'KOTAKBANK',
    'HINDUNILVR', 'AXISBANK', 'SBIN', 'BAJFINANCE', 'BHARTIARTL', 'MARUTI', 'LT',
    'WIPRO', 'ONGC', 'SUNPHARMA', 'TATASTEEL', 'HCLTECH', 'NTPC', 'POWERGRID',
    'TECHM', 'ULTRACEMCO', 'NESTLEIND', 'TITAN', 'DRREDDY', 'HEROMOTOCO'
]))

# Initialize lists for new data
TC, FC, LP, DH, DL, W52H, W52L, VOL, CHG, MA, SE, IND, BAS = ([] for _ in range(13))

nse = NseIndia()

for symbol in top_companies:
    print(f"Processing {symbol}...")
    try:
        (TCap, FCap, LPrice, DayHigh, DayLow, Wk52High, Wk52Low, Volume, ChangePerc, Macro, Sector, Industry, BIndustry) = nse.get_stock_info(symbol)
        
        TC.append(TCap)
        FC.append(FCap)
        LP.append(LPrice)
        DH.append(DayHigh)
        DL.append(DayLow)
        W52H.append(Wk52High)
        W52L.append(Wk52Low)
        VOL.append(Volume)
        CHG.append(ChangePerc)
        MA.append(Macro)
        SE.append(Sector)
        IND.append(Industry)
        BAS.append(BIndustry)
        
        time.sleep(1)  # Avoid rate limiting
    except Exception as e:
        print(f"Failed to process {symbol}: {e}")

# Create DataFrame
df_info = pd.DataFrame({
    'Company': top_companies,
    'TotalCap': TC,
    'FFCap': FC,
    'LastPrice': LP,
    'DayHigh': DH,
    'DayLow': DL,
    '52WkHigh': W52H,
    '52WkLow': W52L,
    'Volume': VOL,
    'ChangePerc': CHG,
    'Macro': MA,
    'Sector': SE,
    'Industry': IND,
    'BasicIndustry': BAS
})

# Save DataFrame
df_info.drop_duplicates(inplace=True)
df_info.to_csv('top_companies_extended_info.csv', index=False)
print("Data saved to top_companies_extended_info.csv")
