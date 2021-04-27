from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import base64
from pprint import pprint

value_gog = str(input('Enter Value: '))



browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.google.com/')
sleep(1)
search = browser.find_element_by_name('q')

value_gog = list(value_gog)
for i in value_gog:
    search.send_keys(i)
    sleep(0.1)

search.send_keys( Keys.RETURN)

sleep(0.5)
image_btn = browser.find_element_by_class_name('MUFPAc').find_element_by_tag_name('a')
image_btn.click()

sleep(0.2)


first_img = browser.find_element_by_class_name('rg_i')


src_img = first_img.get_attribute('src')
img = src_img.split(',')
img_b = bytes(img[1],encoding='utf8')

save_img = open(f'images/first1.jpeg', 'wb')
save_img.write(base64.decodebytes(img_b))
save_img.close()

browser.quit()
