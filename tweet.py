from selenium import webdriver
from random import randrange
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

credentials=open("credentials.txt")
data=credentials.readlines()
pwd=data[1]
userinfo=data[0]
tweet_tags="#NEP2020 #Galgotiasuniversity @DrRPNishank @EduMinOfIndia @DGalgotia @GalgotiasUni "
options = Options()
#options.add_argument('--headless')
options.add_argument('--profile-directory=Default')
options.add_argument("user-data-dir=selenium")
driver=webdriver.Chrome(options=options,executable_path="/home/cipher/Desktop/tweet_bot/chromedriver_linux64/chromedriver")
'''username='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'

driver.find_element_by_xpath(username).send_keys(userinfo)
driver.find_element_by_xpath(password).send_keys(pwd)
driver.find_element_by_xpath(login).click()
sleep(5)'''
driver.get("https://twitter.com")
sleep(5)
f=open("quotes.txt")
for word in f.readlines():
    if word=="\n" or len(word)>200:
        continue
    twee_xpath='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/svg'
    message_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    post_tweet='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
    #logout_click='//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div/div'

    #driver.find_element_by_xpath(twee_xpath).click()
    driver.find_element_by_xpath(message_xpath).send_keys(word+tweet_tags)
    sleep(1)
    driver.find_element_by_xpath(post_tweet).click()
    sleep(2)
    '''driver.get("https://twitter.com/logout")
    sleep(0.5)
    driver.find_elements_by_xpath("//*[contains(text(), 'Log out')]")[1].click()
    sleep(1)'''
    sleep(randrange(300))
f.close()
