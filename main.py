import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)
time.sleep(3)

items = driver.find_elements(By.CLASS_NAME, 'WdR1o')

parsed_data = []

for item in items:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct').text
        price = item.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        link = item.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
    except:
        print("произошла ошибка при парсинге")
        continue

    parsed_data.append([title, price, link])

driver.quit()

with open("dl.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название товара', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)
