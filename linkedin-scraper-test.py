from linkedin_scraper import Person, actions
from selenium import webdriver
#driver = webdriver.Chrome('C:/Users/Frienddo/Desktop/htn2020/chromedriver.exe')
#export CHROMEDRIVER=~/chromedriver
driver = webdriver.Chrome()
email = "put ur email here"
password = "put ur password"
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
person = Person('https://www.linkedin.com/in/shirleywangg/', driver=driver)
print(person)
