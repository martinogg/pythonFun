# https://github.com/dsdanielpark/Bard-API/tree/main#auto-cookie-bard

# import urllib2
url = 'google'

#!python

import browser_cookie3
import requests
cj = browser_cookie3.chrome()
#r = requests.get(url, cookies=cj)

# Filter the cookies to only include those from the specified domain
domain_cookies = [cookie for cookie in cj if (url in cookie.domain and "__Secure-1PSID" == cookie.name)]
#print(domain_cookies);
# Print the cookies
for cookie in domain_cookies:
    print(cookie.name, cookie.value)

# print(cj);