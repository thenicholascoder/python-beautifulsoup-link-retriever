# import BeautifulSoup library, read data from the net
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#use input function then save value inside url
url = input('Enter - ')

#open the url using urllib library (urllib.request.urlopen(variable))
#then do a .read(), 
html = urllib.request.urlopen(url).read()

#tell BeautifulSoup to parse it using .parser, then save return an object
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags in the documemt
tags = soup('a')

#use definite loop for each tags
for tag in tags:

	#get href key or None 
	print(tag.get('href', None))