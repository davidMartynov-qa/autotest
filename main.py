import time

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver


def test_first_test():
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1400,1000)
    driver.implicitly_wait(3)
    driver.get("https://edadeal.ru/")

    # Поиск элемента потверждение города и клик по этой кнопке.
    item_name = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[1]/div/div")
    item_name.click()

    # Поиск элемента search и действия с формой
    input_search = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/header/span/div/div[2]/form/div/div/input")
    input_search.send_keys("Молоко")

    # Клик по форме после действия с формой
    btn_search = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/header/span/div/div[2]/form/button")
    btn_search.click()

    # Поиск кнопки товара и клик по этой кнопке
    item_add_button = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/a[1]")
    item_add_button.click()
    time.sleep(3)
    
    # Описание товара
    title_text = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]")

    title_text2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]")


    assert title_text.text == "Молоко Экомилк пастер., жирн. 3,2%, 93 мл"
    assert title_text2.text == "ПродуктыМолочные продуктыМолоко"

if __name__ == '__main__':
    test_first_test()