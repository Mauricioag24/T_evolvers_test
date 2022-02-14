import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 

options = Options()
options.add_argument("--disable-notifications")
driver= webdriver.Chrome(executable_path=ChromeDriverManager().install(),chrome_options=options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
time.sleep(2)
deploy = driver.find_elements_by_xpath("//a[@class='list-group-item']")
deploy.pop(0)

def change_page(i):
    """Change the Category 

    :param i: Category number
    :type i: int
    """
    deploy = driver.find_elements_by_xpath("//a[@id='itemc']")
    driver.execute_script('arguments[0].click();', deploy[i])
    time.sleep(1)
    return

def add_to_car():
    """Press "add to car" button in each product 
    """
    elements = driver.find_elements_by_xpath("//a[@class='btn btn-success btn-lg']")
    driver.execute_script('arguments[0].click()', elements[0])
    time.sleep(1)
    driver.switch_to.alert.accept()
    ret = driver.find_elements_by_xpath("//img[@src='bm.png']")
    print (ret)
    driver.execute_script('arguments[0].click();', ret[0])
    return


def select_product(j):
    """Chose product in each category. Select 2 products per category

    :param j: Category number
    :type j: int
    """
    elements = driver.find_elements_by_xpath("//a[@class='hrefch']")
    for i in range(2):
        driver.execute_script('arguments[0].click();', elements[i])
        add_to_car()
        change_page(j)
        elements = driver.find_elements_by_xpath("//a[@class='hrefch']")
        time.sleep(1)
    return 


items = len(deploy)
for i in range(items):
    change_page(i)
    select_product(i)
    time.sleep(1)

cart = driver.find_element_by_xpath("//a[@id='cartur']")
driver.execute_script('arguments[0].click();', cart)
time.sleep(4)
driver.close()