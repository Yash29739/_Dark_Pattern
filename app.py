
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = 'https://www.calculator.net/random-number-generator.html'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Get the title of the webpage
    title = soup.title
    print("Title:", title.text)

    # Example: Find all paragraphs on the page
    p = soup.find_all('p')
    # for div in div:
    print("p: ", p)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
