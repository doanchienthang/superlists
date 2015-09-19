from selenium import webdriver
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

browser = webdriver.Firefox()
browser.get('http://localhost:8080')

assert 'Django' in browser.title

# from pyvirtualdisplay import Display
# from selenium import webdriver

# display = Display(visible=0, size=(1024, 768))
# display.start()

# browser = webdriver.Firefox()
# browser.get('http://localhost:8080/polls/')
# print(browser.page_source)

browser.close()
display.stop()