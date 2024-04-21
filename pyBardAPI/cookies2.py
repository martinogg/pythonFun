import browser_cookie3
import requests
url = 'https://bard.google.com'
cj = browser_cookie3.chrome(domain_name=url)
r = requests.get(url, cookies=cj)
print(r.content)