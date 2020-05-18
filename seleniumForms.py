from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"C:\myPrograms(x86)\chromedriver_win32\chromedriver.exe")

browser.get('https://login.metafilter.com')

# finds and fills out username
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('DragonsFuckingCars')

# finds and fills out password
passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('1111')

passwordElem.submit()

#--------------- Sending Special Keys ------------------

from selenium.webdriver.common.keys import Keys

htmlElem = browser.find_element_by_tag_name('html')

# scrolls to bottom
htmlElem.send_keys(Keys.END)

# scrolls to top
htmlElem.send_keys(Keys.HOME)

#browser.back()  # back btn
#browser.forward()  # forward btn
#browser.refresh()  # refresh btn
browser.quit() # quit btn