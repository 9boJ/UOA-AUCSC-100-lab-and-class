import requests # Error 1: Incorrect import
# Changed "request" to "requests"

from bs4 import BeautifulSoup # Error 2: Incorrect case
# Changed "Beautifulsoup" to "BeautifulSoup"

url = "https://example.com"
response = requests.get(url) # Error 3: Incorrect import usage
# Changed "request" to "requests"

soup = BeautifulSoup(response.text, 'html.parser') # Error 4: Incorrect case
# Changed "Beautifulsoup" to "BeautifulSoup"

headings = soup.findAll('h1')
print("Headings found:")
for heading in headings: # Error 5: Missing colon
# Add a colon at the end 
    print(heading.text)
