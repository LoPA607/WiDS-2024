import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website
url = "https://www.moneycontrol.com/news/business/markets/"

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract news headlines and links (example class, may need adjustment)
articles = soup.find_all('li', class_='clearfix')

data = []
for article in articles:
    headline = article.find('h2').text.strip() if article.find('h2') else 'No headline'
    link = article.find('a')['href'] if article.find('a') else 'No link'
    summary = article.find('p').text.strip() if article.find('p') else 'No summary'
    data.append({'Headline': headline, 'Link': link, 'Summary': summary})

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('financial_news2.csv', index=False)
print("Data saved to financial_news2.csv")

df = pd.read_csv('financial_news2.csv')

# List to store detailed information
detailed_info = []

# Iterate through each link in the CSV
for index, row in df.iterrows():
    link = row['Link']
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the required information from the link
    # Example: Extracting the title and publication date
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title'
    publication_date = soup.find('time').get_text(strip=True) if soup.find('time') else 'No date'
    
    # Append the information to the list
    detailed_info.append({
        'Title': title,
        'Publication Date': publication_date,
        'Link': link
    })

# Create a DataFrame with the detailed information
df_detailed_info = pd.DataFrame(detailed_info)

# Save the detailed information to a new CSV file
df_detailed_info.to_csv('detailed_financial_news.csv', index=False)

print(df_detailed_info)

df = pd.read_csv('detailed_financial_news.csv')

# List to store detailed information
detailed_info = []

# Iterate through each link in the CSV
for index, row in df.iterrows():
    link = row['Link']
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the required information from the link
    # Example: Extracting the title, publication date, and article content
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title'
    publication_date = soup.find('time').get_text(strip=True) if soup.find('time') else 'No date'
    article_content = ' '.join([p.get_text(strip=True) for p in soup.find_all('p')])
    
    # Append the information to the list
    detailed_info.append({
        'Title': title,
        'Publication Date': publication_date,
        'Link': link,
        'Content': article_content
    })

# Create a DataFrame with the detailed information
df_detailed_info = pd.DataFrame(detailed_info)

# Save the detailed information to a new CSV file
df_detailed_info.to_csv('detailed_financial_news_with_content.csv', index=False)

print(df_detailed_info)