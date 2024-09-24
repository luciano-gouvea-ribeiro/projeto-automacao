import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# Buscando o Drive do navegador e abrindo o nagedador
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
servico = Service(ChromeDriverManager().install()) 
navegador = webdriver.Chrome(service=servico)


# entrando no site para fazer login.
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

# acessando o login do site
navegador.find_element('xpath', '//*[@id="email"]').send_keys('emialfiquiticio@outlook.com')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="password"]').send_keys('12345678')
time.sleep(1)
navegador.find_element('xpath', '//*[@id="pgtpy-botao"]').click()

# abrindo o arquivo csv
with open('produtos.csv', mode='r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    next(leitor_csv)
    
    for linha in leitor_csv:
        # Prenchendo o nome do codigo:
        campo_nome = navegador.find_element('xpath', '//*[@id="codigo"]' ).send_keys(linha[0])
        time.sleep(0.5)
        # Preenchendo a marca do produto
        campo_marca = navegador.find_element('xpath', '//*[@id="marca"]' ).send_keys(linha[1])
        time.sleep(0.5)
        # Preenchendo o tipo de produto    
        campo_tipo = navegador.find_element('xpath', '//*[@id="tipo"]' ).send_keys(linha[2])
        time.sleep(0.5)
        # Preenchendo a categoria do produto
        campo_categoria = navegador.find_element('xpath', '//*[@id="categoria"]' ).send_keys(linha[3])
        time.sleep(0.5)
        # Preenchendo o preço do produto
        canpo_preco = navegador.find_element('xpath', '//*[@id="preco_unitario"]' ).send_keys(linha[4])
        time.sleep(0.5)
        # Preenchendo o custo do produto
        canpo_custo = navegador.find_element('xpath', '//*[@id="custo"]' ).send_keys(linha[5])
        time.sleep(0.5)

        # Verifdicando se no campo obs está vazio ou não:
        if linha[6] is None:
            next
        else:
            canpo_obs = navegador.find_element('xpath', '//*[@id="obs"]' ).send_keys(linha[6])
            time.sleep(2)
    
        # clicando no botão de enviar
        navegador.find_element('xpath', '//*[@id="pgtpy-botao"]').click()

# fechando o navegador
navegador.quit()

