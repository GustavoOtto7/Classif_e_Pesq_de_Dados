from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Função para configurar o navegador
def setup_driver():
    chrome_driver_path = "C:/Program Files/Google/chromedriver-win64/chromedriver.exe"
    service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

# Função para rolar a página e carregar as ofertas
def load_all_offers(driver, url):
    driver.get(url)
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Função para extrair os dados dos produtos
def extract_product_data(driver):
    titles, prices, discounts = [], [], []
    
    try:
        product_grid = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'prodarea'))
        )
        products = product_grid.find_elements(By.CLASS_NAME, 'product-item')

        for product in products:
            # Extrair título
            title_element = product.find_element(By.CLASS_NAME, 'prod-name')
            title = title_element.text.strip()
            titles.append(title)

            # Extrair preço
            price_element = product.find_element(By.CLASS_NAME, 'prod-new-price')
            price_span = price_element.find_element(By.TAG_NAME, 'span')
            price_clean = price_span.text.replace('R$ ', '').replace('.', '').replace(',', '.').strip()
            price_float = float(price_clean)
            prices.append(price_float)

            # Extrair desconto
            try:
                discount_element = product.find_element(By.CLASS_NAME, 'colPorcent')
                discount_div = discount_element.find_element(By.TAG_NAME, 'div')
                discount_str = discount_div.text.strip().replace('%', '')
                discount_int = int(discount_str)
            except:
                discount_int = 0
            discounts.append(discount_int)

    except Exception as e:
        print(f"Erro ao encontrar os produtos: {e}")
    
    return titles, prices, discounts

# Função de ordenação BubbleSort para preços
def bubblesort(titles, prices):
    n = len(prices)
    for i in range(n):
        for j in range(0, n-i-1):
            if prices[j] > prices[j+1]:
                # Trocar os preços
                prices[j], prices[j+1] = prices[j+1], prices[j]
                # Trocar os títulos para manter a correspondência
                titles[j], titles[j+1] = titles[j+1], titles[j]
    return titles, prices

# Função principal
def main():
    driver = setup_driver()
    url = 'https://www.terabyteshop.com.br/promocoes'
    
    try:
        load_all_offers(driver, url)
        titles, prices, discounts = extract_product_data(driver)

        # Exibir os detalhes completos antes da ordenação
        print("Detalhes dos produtos antes da ordenação:\n")
        for i in range(len(titles)):
            print(f"Título: {titles[i]}")
            print(f"Preço: R$ {prices[i]:.2f}")
            print(f"Desconto: {discounts[i]}%\n")

        # Ordenar os preços usando BubbleSort (mantendo a correspondência com os títulos)
        sorted_titles, sorted_prices = bubblesort(titles.copy(), prices.copy())

        # Exibir título e preço após a ordenação
        print("\nProdutos após a ordenação por preço (crescente):")
        for i in range(len(sorted_titles)):
            print(f"{sorted_titles[i]} - R$ {sorted_prices[i]:.2f}")
    finally:
        driver.quit()
main()