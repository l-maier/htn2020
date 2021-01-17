from linkedin_scraper import Person, actions
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class LinkedinScraper:

    def __init__(self, email, password):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome('C:/Users/Frienddo/Desktop/htn2020/chromedriver.exe')
        actions.login(self.driver, email, password) # if email and password isnt given, it'll prompt in terminal
        self.person = None
    
    def scrap(self, url):
        self.person = Person(url, driver=self.driver)
        #print(self.person)
    
    def getAbout(self):
        if self.person is not None and self.person.about is not []:
            return str(self.person.about[0])
        else:
            return ''

    def getEducation(self):
        if self.person is not None and self.person.educations is not []:
            return str(self.person.educations[0])
        else:
            return ''
        
    def getCompany(self):
        if self.person is not None and self.person.company:
            return str(self.person.company)
        else:
            return ''

    def getTitle(self):
        if self.person is not None:
            return str(self.person.job_title)
        else:
            return ''

