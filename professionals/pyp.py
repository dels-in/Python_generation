from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text(strip=True)

print(text)

import requests
response = requests.get('https://stepik.org/lesson/569748/step/5?unit=564262')
print (*response.content.split(), sep="\n")