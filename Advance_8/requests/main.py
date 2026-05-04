import requests
import bs4 # BeautifulSoup for parsing HTML

response = requests.get("https://deepakprasad.xyz")
soup = bs4.BeautifulSoup(response.text, 'html.parser')

print(soup.title)  # <title>Deepak Prasad</title>
print(soup.title.string)  # Deepak Prasad

for link in soup.find_all('a'):
    print(link.get('href'))  # Print all hyperlinks on the page

# print(response.status_code)  # 200
# print(response.headers)      # Response headers
# print(response.text)         # HTML content of the page


url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
   }
response = requests.post(url, json=data, headers=headers)
print(response.status_code)  # 201
print(response.json())       # Response JSON (new post details)