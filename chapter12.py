# import BeautifulSoup library, read data from the net
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#use input function then save value inside url
url = "http://py4e-data.dr-chuck.net/comments_373679.html"

#open the url using urllib library (urllib.request.urlopen(variable))
#then do a .read(),
html = urllib.request.urlopen(url).read()

#tell BeautifulSoup to parse it using .parser, then save return an object
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags in the documemt
tags = soup('span')

#variables
count = 0
sum = 0

#use definite loop for each tags
for tag in tags:

	#take the text inside the tag between <span></span>
	x = int(tag.text)

	#itterate previous value and current value
	count += 1

	#summation of values between the <span></span> tag which is the x variable
	sum = sum + x

#print the count of tags
print(count)

#print the summation of text on the tags which are numbers
print(sum)