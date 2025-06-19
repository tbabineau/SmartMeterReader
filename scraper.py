import credentials
import requests
from bs4 import BeautifulSoup




#Logging in to the page
login_url = "https://www.nbpower.com/Auth/WebLogin.aspx?ReturnUrl=%2fCustomer%2fViewConsumptionGraph.aspx"
success_title = 'Consumption History'
payload = {
    "Username": credentials.user,
    "Password": credentials.pwd
}
#POSTing login info. needs to have language cookie or it will not work
response = requests.post(login_url, data=payload, cookies={'lang':'en'})

#Data received
if response.ok:
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find('title')

    if title != None:
        title = title.text.strip()
        if title == success_title:
            print("Login Successful")
            print(soup)
        else:
            pass
            print("Issue with login")
            #print(response.text)
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