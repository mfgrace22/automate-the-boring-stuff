# import the python requests library
# in order to make requests to servers
import requests
# Beautiful Soup is a library that makes it easy to scrape information from web pages.
import bs4

# save Response object in a variable called response
# use requests library to issue a get request to the
# specified URL
response = requests.get(
	url="https://en.wikipedia.org/wiki/Web_scraping",
)

# print the response object
print(f'RESPONSE OBJECT: {response}')
# print the response status code
print(f'STATUS CODE: {response.status_code}')
# print the response in json format
# print(f'JSON: {response.json()}')

