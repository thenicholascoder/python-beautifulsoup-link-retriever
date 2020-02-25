# import BeautifulSoup library, read data from the net
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#use input function then save value inside url, cound and position
url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))

#itterate how many times this definite loop will repeat
for i in range(count):

	#open the url using urllib library (urllib.request.urlopen(variable))
	#then do a .read(),
	html = urllib.request.urlopen(url).read()

	#tell BeautifulSoup to parse it using .parser, then save return an object
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags in the documemt
	tags = soup('a')

	#variables
	names = list()
	urls = list()

	#use definite loop for each tags
	for tag in tags:
		#take the url inside the href between <a></a> tag
		x = tag.get('href', None)

		#the resulting url, append it to the dictionary names
		names.append(x)

		#take the text inside the tag between <a></a> tag
		y = tag.text

		#the resulting y, append it to the dictionary urls
		urls.append(y)

	#manipulate the url variable with the last data inside the names list
	url = str(names[position-1])

	#print the last name retrieved
	print(urls[position-1])s