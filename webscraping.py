from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from pyautogui import press, hotkey
from pyperclip import copy
from time import sleep

driver = Chrome()
driver.get('https://censo2022.ibge.gov.br/panorama/?utm_source=ibge&utm_medium=home&utm_campaign=portal')
sleep(1)

select_element = driver.find_element('css selector', '#autocomplete')
select = Select(select_element)

options = [element.text for element in select.options[:33]]

for option in options:
    element = driver.find_element('css selector', '#select2-autocomplete-container')
    element.click()
    sleep(1)

    copy(option)
    hotkey('ctrl', 'v')
    sleep(1)
    press('enter')
    sleep(2)

    for i in (0, 3):
        for selector in ('#chartDownloadBtn', '#downloadXLSX'):
            elements = driver.find_elements('css selector', selector)
            elements[i].click()
            sleep(1)
