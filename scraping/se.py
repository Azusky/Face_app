from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from images import saveImage
# from fs import loadConfig


def searchImagesForName(names, settings, tags, quantity=13):
    browser = webdriver.Chrome(settings['engineBrowser'])
    browser.get(settings['search_url'])
    sleep(settings['search_delay'])

    for name in names:
        for tag in tags[name[0]]:
            search = browser.find_element_by_name(settings['search_input_class'])
            liter = list(name[1] + ' ' + tag)
            # function ?
            search.clear()
            for i in liter:
                search.send_keys(i)
                sleep(0.1)

            search.send_keys( Keys.RETURN)
            ############

            sleep(settings['search_delay'])


            images = browser.find_elements_by_css_selector(settings['result_img_class'])
            for img in images[:quantity]:
                src_img = img.get_attribute('src')
                saveImage(src_img, name[0], name[1], settings['IMAGE_BASE_FOLDER'])

    browser.quit()
