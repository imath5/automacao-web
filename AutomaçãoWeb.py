'''DESAFIO

Você trabalha em uma empresa de venda de serviços de alto valor agregado e seus clientes tem um prazo de pagamento de 30 dias para pagar.
Acontece que, como em quase toda empresa, nem sempre os clientes pagam o valor na data acordada ou nem sempre pagam o valor por completo.
Esses clientes são considerados inadimplentes.
A equipe do setor financeiro faz um controle com o valor devido de cada cliente.
Todos os dias, uma nova planilha dessa é gerada com os clientes que se tornaram inadimplentes naquele dia e
a equipe de atendimento ao cliente precisa entrar em contato, por e-mail, com cada cliente inadimplente para enviar para eles o boleto.
Esse processo é todo feito pela plataforma do banco da empresa (PagSeguro)
Acontece que esse processo é todo feito pelo site do PagSeguro e é um processo bem repetitivo. E tudo que é repetitivo pode ser automatizado.'''

'''1º Organizar em português

• Passo 1: Importar base de dados

• Passo 2: Visualizar a base de dados

• Passo 3: Fazer manualmente o processo no PagSeguro

• Passo 4: Transformar o processo manual em código Python - Para apenas 1 cliente

• Passo 5: Automatizar o processo para todas as pessoas

• Passo 6: Revisar o código e ajustar o que for necessário'''

'''• Passo 1: Importar base de dados

• Passo 2: Visualizar a base de dados'''

import pandas as pd
import time

tabela_clientes = pd.read_excel("Clientes Pagamento.xlsx",dtype ={"Cliente":object})
#tabela_clientes = pd.read_excel("Clientes Pagamento.xlsx",dtype ={"Cliente":object}, sheet_name="")
display (tabela_clientes)

'''  • Passo 3: Fazer manualmente o processo no PagSeguro
  
  1. Entrar no site do PagSeguro.
  2. Fazer login no site do PagSeguro. 
  3. Ir pra página de cobrança de pagamento.
  4. Preencher as informações do cliente.
  5. Clicar em revisar depois de preencher.
  6. Confirmar envio.'''

'''  • Passo 4: Criar o processo em código Python para uma pessoa
   Ex: - Nome: Matheus
       - Devendo: 605
       - Email: matheusdocarvalho+1@gmail.com
   
  Para isso, vamos usar o Selenium - para o Selenium funcionar você precisa baixar o Chrome Driver'''

#Abrindo pagina automatizada
from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get ("https://acesso.pagseguro.uol.com.br/")

#navegador.find_element_by_id    #ENCONTRAR PELO ID(HTML) PELO INSPENCIONAR PÁGINA

#navegador.find_element_by_xpath #ENCONTRAR PELO XPATH *QNDO N TEM ID PELO INSPENCIONAR PÁGINA

#send_keys() #DIGITAR

#click() #CLICKAR'''

navegador.find_element_by_id("user").send_keys("email_da_pessoa@gmail.com")
navegador.find_element_by_id("password").send_keys("senha da pessoa")

navegador.find_element_by_xpath('//*[@id="__next"]/div/div/main/div/div/div/form/div/div/div/div/div[3]/button').click()
time.sleep(5)

# Ir para a página de pagamento
for linha in tabela_clientes.index

    divida = tabela_clientes.loc[linha, "Valor Total Devido"] - tabela_clientes.loc[linha, "Valor Pago"]
    if divida > 0:
        navegador.get("https://pagseguro.uol.com.br/operations/charging/create.jhtml")
    time.sleep(5)

    email = tabela_clientes.loc[linha, "Email"]
    valor = divida
    nome = tabela_clientes.loc[linha, "Nome"]

    # preencher email
    navegador.find_element_by_xpath('link xpath').send_keys(email)

    # nome
    navegador.find_element_by_xpath('link xpath').send_keys(nome)

    # descrição
    navegador.find_element_by_xpath('link xpath').send_keys("Cobrança Pagamento Atrasado")

    # campo valor
    texto_valor = f"{valor:.2f}"
    navegador.find_element_by_xpath('link xpath').send_keys(texto_valor)

    # clicar no botão para enviar
    navegador.find_element_by_xpath('link xpath').click()
    time.sleep(5)

    # clicar no botão de confirmação
    navegador.find_element_by_xpath('link xpath').click()
    time.sleep(5)

'''  • Passo 5: Automatizar o processo para todas as pessoas
  • Passo 6: Revisar o código e ajustar o que for necessário ^'''
