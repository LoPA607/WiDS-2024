# Function to scrape quarterly results
import requests
from bs4 import BeautifulSoup
import pandas as pd

company_name = []
revenue = []
net_profit = []
quarter = []


def scrape_quarterly_results():
    url = 'https://www.moneycontrol.com/financials/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extracting quarterly result data
    results = []
    for result in soup.find_all('div', class_='section_results'):
        company_name = result.find('a', class_='company').text
        revenue = result.find('span', class_='revenue').text
        net_profit = result.find('span', class_='net_profit').text
        quarter = result.find('span', class_='quarter').text

        results.append({
            'Company': company_name,
            'Revenue': revenue,
            'Net Profit': net_profit,
            'Quarter': quarter
        })
        
    return pd.DataFrame(results)

# Fetch quarterly results and save to CSV
df_results = scrape_quarterly_results()
df_results.to_csv('quarterly_results.csv', index=False)
