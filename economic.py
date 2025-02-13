import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Economic Times news page
url = "https://economictimes.indiatimes.com/markets/stocks/news"

# Send a GET request
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the news articles container
    articles = soup.find_all('div', class_='eachStory')
    
    data = []
    for article in articles:
        title_tag = article.find('h3')
        link_tag = article.find('a')
        summary_tag = article.find('p')
        
        if title_tag and link_tag:
            title = title_tag.text.strip()
            link = link_tag['href']
            summary = summary_tag.text.strip() if summary_tag else 'No summary'
            
            # Append the information to the list
            data.append({
                'Title': title,
                'Link': f"https://economictimes.indiatimes.com{link}",
                'Summary': summary
            })
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Save to CSV
    df.to_csv('economic_times_news.csv', index=False)
    print("Data saved to economic_times_news.csv")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


df = pd.read_csv('economic_times_news.csv')

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
df_detailed_info.to_csv('detailed_economic_times_news.csv', index=False)

print(df_detailed_info)