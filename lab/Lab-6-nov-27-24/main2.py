import re as re
# # Sample text
# text = "John's phone number is 123-456-7890. Call him at 987-654-3210."
# # Pattern to match phone numbers
# pattern = r"\d{3}-\d{3}-\d{4}"
# # Find all matches in the text
# matches = re.findall(pattern, text)
# # Display the matches
# print("Phone numbers found:", matches)

# for i in matches:
#     if re.findall("^987", i):
#         print(i)   




# pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}"

# text = "Contact us at support@example.com, sales@company.org, or info@domain.net."

# matches = re.findall(pattern, text)
# print(matches)


# import requests
# from bs4 import BeautifulSoup

# # URL to crawl
# url = "https://example.com"

# # Fetch the webpage
# response = requests.get(url)

# # Parse the webpage content
# soup = BeautifulSoup(response.text, 'html.parser')

# links = soup.find_all("a")
# print("Links found on the webpage:")
# for link in links:
#     print(link.get('href'))

import requests
from bs4 import BeautifulSoup
# Base URL of the blog
base_url = "https://example-blog.com"
# List to store article titles
titles = []
# Crawl the first 3 pages
for page in range(1, 4):
    # Construct the URL
    url = f"{base_url}/page/{page}"
    # Fetch the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract article titles
    articles = soup.find_all('h2', class_='article-title')
    for article in articles:
        titles.append(article.text)
#
#  Display the titles
print("Article Titles Found:")
for title in titles:
    print(title)



