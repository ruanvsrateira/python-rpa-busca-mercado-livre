from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd

pesquisa = input("Oque deseja pesquisar no Mercado Livre ? \n")
lista_de_produtos = []

options = Options()
options.add_argument('--headless')
service =  Service(GeckoDriverManager().install())
browser = webdriver.Firefox(options=options, service=service)
browser.get('https://mercadolivre.com.br')

sleep(5)

search_input = browser.find_element(By.CSS_SELECTOR, '.nav-search-input')
search_input.send_keys(pesquisa)
search_input.submit()

sleep(5)

cards = browser.find_elements(By.CSS_SELECTOR, '.ui-search-result__wrapper')

for card in cards:
    title = card.find_element(By.CSS_SELECTOR, 'div > a').get_attribute('title')
    link_page_item = card.find_element(By.CSS_SELECTOR, 'div > a').get_attribute('href')
    
    container_prices = card.find_element(By.CSS_SELECTOR, 'div > a > div.ui-search-result__content-wrapper')

    price_now = container_prices.find_element(By.CSS_SELECTOR, '.price-tag-fraction').text
    price_now = f'R$ {price_now}'

    lista_de_produtos.append([title, link_page_item, price_now])

dados = pd.DataFrame(lista_de_produtos, columns=['title', 'link do produto', 'preço em reais'])

dados.to_json('lista.json', index=False)
    