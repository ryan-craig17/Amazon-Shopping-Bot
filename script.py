#get your Chrome driver from the link below
# https://sites.google.com/a/chromium.org/chromedriver/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
import schedule

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG/ref=sr_1_1?dchild=1&keywords=ps5&qid=1608263723&rnid=2941120011&s=videogames&sr=1-1") 
#enter Amazon URL here^

def func():
#Click Add To Cart
    try:
        search = driver.find_element_by_name("submit.add-to-cart").click()
    except:
        print("Not In Stock Yet!")
    else:
#Proceed to Checkout
        cart = driver.find_element_by_id("hlb-ptc-btn-native").click()
#Enter Email
        name = driver.find_element_by_name("email")
        name.send_keys("") #enter email address here
        name.send_keys(Keys.RETURN)
#Enter Password
        password= driver.find_element_by_name("password")
        password.send_keys("") #enter password here
        password.send_keys(Keys.RETURN)
#Place Order
        place = driver.find_element_by_name("placeYourOrder1").click()
        time.sleep(10)
        driver.quit()

schedule.every(5).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)
