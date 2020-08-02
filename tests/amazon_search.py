from selenium import webdriver


def test_setup():
    global driver
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    driver.set_page_load_timeout(10)
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_load_amazon():
    driver.get("https://www.amazon.in/")
    x = driver.title
    driver.find_element_by_id("twotabsearchtextbox").send_keys("oneplus")
    driver.find_element_by_xpath("//input[@value='Go']").click()
    print("title" + x)
    assert x == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"


def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")

