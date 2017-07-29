import mechanize
from bs4 import BeautifulSoup as bs

url = 'http://www.jne.co.id/id/tracking/trace'

br = mechanize.Browser()
br.open(url)

response = br.response()

soup = bs(response.read(), "html5lib").find("form", class_="contact_form")

print soup # URL of the page we just opened
