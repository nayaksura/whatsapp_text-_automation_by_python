import datetime
import sched, time
from selenium import webdriver 

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('C:\\Users\\suraj\\Downloads\\chromedriver.exe') 

driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

    # Replace 'Friend's Name' with the name of your friend 
    # or the name of a group 
target = '"name of the friend"'

    # Replace the below string with your own message 
string = "Happy birthday!!!"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
group_title.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    

input_box = wait.until(EC.presence_of_element_located(( 
        By.XPATH, inp_xpath)))
birthday = datetime.datetime(2020, 6, 4, 21, 6, 0)
# enter the birthdate and the time you want him / her to wish
while datetime.datetime.now() < birthday:
    time.sleep(1)
#set the range for number of times you want to send the message

for i in range(10): 
    input_box.send_keys(string + target + Keys.ENTER) 
    time.sleep(1) 

