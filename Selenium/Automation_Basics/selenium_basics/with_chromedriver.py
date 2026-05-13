

from selenium import webdriver
from selenium.webdriver.edge.service import Service
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser = input("What browser do you want to use? ")

match (browser.lower()):
    case 'chrome':
        driver = webdriver.Chrome(service = Service('../resources/chromedriver.exe'))

    case 'edge':
        driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

# Open Google
driver.get("https://www.google.com")

pagetitle = driver.title

if pagetitle == 'Google':
    print("Hurray!! Google HomePage Loaded - Pass")
else:
    print("Google Homepage Not loaded")

driver.quit()