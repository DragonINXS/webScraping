from selenium import webdriver
browser = webdriver.Chrome(executable_path=r"C:\myPrograms(x86)\chromedriver_win32\chromedriver.exe")

type(browser)

browser.get('https://inventwithpython.com/')

# finds elements by class name
#try:
#    elem = browser.find_element_by_class_name('btn')
#    print('Found <%s> element with that class name!' % (elem.tag_name))
#except:
#    print('Was not able to find an elemnet with that name.')

# clicks an element it finds
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()