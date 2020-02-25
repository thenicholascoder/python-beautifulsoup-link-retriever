# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#import urllib library
import urllib.request, urllib.parse, urllib.error

#from bs4 folder, import BeautifulSoup library
from bs4 import BeautifulSoup

#import ssl library
import ssl

#Just add this, this is to ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#create input then store it to url
url = input('Enter - ')

#using urllib library open the file, add context=ctx because it is for https
#you can remove it but it would not be https, then read() will convert to string
#save them all inside html variable
#steps = library,request,open.read()
#this basically means read the url variable with https certification
html = urllib.request.urlopen(url, context=ctx).read()

#BeautifulSoup will get all the html tags then will store it as object inside soup
soup = BeautifulSoup(html, 'html.parser')

#Retrieve me all the anchor tags which is <a></a>
tags = soup('a')

#for each tag in tags = <a></a>
for tag in tags:

	#print me the value of 'href' inside that anchor tags or None
    print(tag.get('href', None))
