import time
from selenium import webdriver
txt=open(r'Countries.txt','r')

countries=txt.read()

txt.close()
country =countries.split('\n')
print(country)

browser = webdriver.Firefox()

browser.get('https://www.jetpunk.com/quizzes/how-many-countries-can-you-name')
browser.find_element_by_css_selector("#start-button").click()
field=browser.find_element_by_css_selector('#txt-answer-box')
for word in country:
    if len(word)>1:
        field.send_keys(word)
        #time.sleep(0.1)
