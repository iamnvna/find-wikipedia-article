import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text

    print(f"{title} \nDo you want to view it? (Y/N) ")
    ans = input("").lower()

    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open_new_tab(url)
        break
    elif ans == "n":
        print("Try again!")
        continue
    else:
        print("Wrong choice!")
        break

# Commentary
'''
Line 1-3:
    The necessary python module required to run this program are imported
    before the code is written. requests allows us to get data from a
    particular website. BeautifulSoup allows the parsing of that data to
    select specific information. webbrowser allows us to control the default
    web browser on the system or pass actions over to it.
    
Line 6-8:
    The variable url holds the url to the Wikipedia random article url. A
    variable soup is created to hold the url content from the url variable
    parsed as an html. The title variable then holds the title of the
    random article from wikipedia using the soup.find method.
    
Line 10-11:
    The title from line 8 is printed to screen, and the user is asked if they
    want to view it. The answer is converted to lowercase using the .lower()
    method.
    
Line 13-22:
    This block of code is a series of if/elif/else statements that iterate through
    the user input from line 10. If the user responds yes to reading the article,
    a url variable is created to hold the default path to a wikipedia article, appended
    by the title variable (which holds the title of the random article) from line 8.
    The webbrowser module is called to work here to open the url in a new tab. The
    program prints try again when the user answers no the question in line 10, and
    quits the program after an invalid input.
'''