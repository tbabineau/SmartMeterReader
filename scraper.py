import credentials
import requests
from bs4 import BeautifulSoup

#Logging in to the page
login_url = "https://www.scrapingcourse.com/login"
success_title = "Success Page - ScrapingCourse.com"
payload = {
    "email": credentials.user,
    "password": credentials.pwd
}

#POSTing login info
response = requests.post(login_url, data=payload)

#Data received
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title')
    if title == None: #Incase the tags are uppercase, may be able to do in regex
        title = soup.find('TITLE')

    if title != None:
        title = title.text
        if title == success_title:
            print("Login Successful")
        else:
            print("Issue with login")
    else:
        print("No title")
#Issue sending info
else:
    print("Issue with webpage")

"""

#Grabbing the HTML from the page
url = ''
response = requests.get(url)
#If we get a 2xx
if response.ok:
    soup = BeautifulSoup(response.content, "html.parser")
    '''
    by id: soup.find(id = 'ID')
    by tag: soup.find('tag')
    by class: soup.find(class_='class')
    by attribute: soup.find(attr={'attrName":"name"})
    returns None if nothing is found
    '''
#Otherwise, error. Print the error
else:
    print(response)
"""