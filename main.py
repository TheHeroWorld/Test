from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    articul = input("Введите артикул:\n")
    name = input("Введите название:\n").lower()
    url = f"https://www.wildberries.ru/catalog/{articul}/detail.aspx"
    driver = webdriver.Chrome()

    try:
        driver.get(url)
        driver.implicitly_wait(10)
        title_element = driver.find_element(By.CSS_SELECTOR, "h1.product-page__title")
        title_text = title_element.text.strip().lower() 
        if name in title_text:
            print(f"Название товара:{title_element.text.strip()},\n ссылка на товар:{url}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
