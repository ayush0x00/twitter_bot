from selenium import webdriver
from random import randrange
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

credentials=open("credentials.txt")
tweet_tags="#NEP2020 #Galgotiasuniversity @DrRPNishank @EduMinOfIndia @DGalgotia @GalgotiasUni "
options = Options()
#options.add_argument('--headless')
options.add_argument("user-data-dir=selenium")
options.add_argument('--profile-directory=Default')
driver=webdriver.Chrome(options=options,executable_path="/home/cipher/Desktop/tweet_bot/chromedriver_linux64/chromedriver")
f=open("quotes.txt")
for word in f.readlines():
    if word=="\n" or len(word)>200:
        continue
    driver.get("https://twitter.com/login")
    sleep(5)

    username='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    password='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    login='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'

    driver.find_element_by_xpath(username).send_keys(credentials.readlines()[0])
    driver.find_element_by_xpath(password).send_keys(credentials.readlines()[1])
    driver.find_element_by_xpath(login).click()
    sleep(5)


    message_xpath='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
    post_tweet='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
    sleep(5)

    logout_click='//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div/div'

    driver.find_element_by_xpath(message_xpath).send_keys(word)
    sleep(1)
    #driver.find_element_by_xpath(post_tweet).click()
    sleep(0.5)
    driver.get("https://twitter.com/logout")
    sleep(0.5)
    driver.find_elements_by_xpath("//*[contains(text(), 'Log out')]")[1].click()
    sleep(1)
    driver.quit()
    sleep(randrange(300))
f.close()
