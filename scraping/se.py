from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from images import saveImage
from fs import loadConfig

settings = loadConfig('settings')

def searchImagesForName(name, settings,  quantity=13):
    browser = webdriver.Chrome(settings['engineBrowser'])
    browser.get(settings['search_url'])
    sleep(settings['search_delay'])
    # img_btn_selected = False


    value_gog = name
    search = browser.find_element_by_name(settings['search_input_class'])

    value_gog = list(value_gog)
    search.clear()
    for i in value_gog:
        search.send_keys(i)
        sleep(0.1)

    search.send_keys( Keys.RETURN)

    # sleep(0.5)
    # if not img_btn_selected:
    #     image_btn = browser.find_element_by_class_name(settings['search_filter_image_btn_class'][0]).find_element_by_tag_name(settings['search_filter_image_btn_class'][1])
    #     image_btn.click()
    #     img_btn_selected = True
    sleep(settings['search_delay'])


    images = browser.find_elements_by_css_selector(settings['result_img_class'])
    for img in images[:quantity]:
        src_img = img.get_attribute('src')
        saveImage(src_img, name, settings['IMAGE_BASE_FOLDER'])
