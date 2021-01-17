from linkedin_scraper import Person, actions
from selenium import webdriver

class LinkedinScraper:

    def __init__(self, email, password):
        self.driver = webdriver.Chrome('C:/Western/LinkedinRoast/htn2020/chromedriver.exe')
        actions.login(self.driver, email, password) # if email and password isnt given, it'll prompt in terminal
        self.person = None
    
    def scrap(self, url):
        self.person = Person(url, driver=self.driver)
        print(self.person)
    
    def getAbout(self):
        if self.person is not None and self.person.about is not []:
            return str(self.person.about[0])
        else:
            return ''