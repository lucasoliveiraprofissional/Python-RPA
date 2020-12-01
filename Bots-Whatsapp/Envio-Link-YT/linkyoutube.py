from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyperclip
'''O pyperclip é pq caso o contato/grupo tenha emojis na definição, 
o sendkeys não conseguirá reproduzir esse caractere de emoji'''

with open('groups.txt', 'r', encoding='utf8') as f:
  groups = [group.strip() for group in f.readlines()]

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

browser.get('https://web.whatsapp.com/')

LinkYT = 'https://www.youtube.com/watch?'


for group in groups:
  #Achar o campo de busca
  search_path = '//div[contains(@class,"copyable-text selectable-text")]'
  
  search_box = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.XPATH, search_path))
  )

  search_box.clear()

  #Copiar do arquivo texto o nome do contato/grupo
  pyperclip.copy(group)

  #Colar o nome do contato/grupo no campo de busca
  search_box.send_keys(Keys.CONTROL + "v")

  #Esperar um tempo pra que os servers do Whats não
  #suspeitem que é um bot mesmo
  sleep(2)

  #Achar o caminho onde está o contato/grupo
  #(Atualmente consegui sucesso clicando na foto do usuário, não testei nesse robo ainda)
  group_xpath = f'//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[1]/div/div/span'
  group_title = browser.find_element_by_xpath(group_xpath)

  sleep(1)

  #Clicar no resultado da busca
  group_title.click()

  sleep(1)

  #Achar o campo de texto pra digitar a mensagem
  input_xpath= '//div[contains(@class,"copyable-text selectable-text")]'
  input_box = browser.find_elements_by_xpath(input_xpath)

  #Enviar link com pré-visualização:
  input_box[1].send_keys(LinkYT)
  sleep(4)

  #Ver a pre-visualização antes de enviar:
  pre_xpath = '//*[@id="main"]/footer/div[2]/div/div[5]/div[1]/div[1]/div/div'
  pre = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.XPATH, pre_xpath))
  )

  sleep(1)

  input_box[1].send_keys(Keys.ENTER)
  
  sleep(2)


#Desconectar da sessão aberta no Whatsapp Web
#Primeiro Clicará no menu com 3 pontos na vertical
menu_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
menu = browser.find_element_by_xpath(menu_xpath)
menu.click()

sleep(1)

#Depois de esperar as opções do menu aparecerem,
#clicará na opção: "Desconectar".
descon_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[7]/div'
descon = browser.find_element_by_xpath(descon_xpath)
descon.click()

sleep(1)

#Por fim, encerrará a instância do Browser ativa:
browser.quit()

''' 
Opções de Xpath caso o utilizado para a pré-visualização do vídeo não funcione:

Toda a mensagem estar visível xpath
'//*[@id="main"]/div[3]/div/div/div[3]/div[11]/div/div[1]/div'

Titulo do vídeo estar visível xpath
//*[@id="main"]/div[3]/div/div/div[3]/div[11]/div/div[1]/div/div[1]/div[1]/div/a/div[1]

Link do vídeo estar visível xpath
//*[@id="main"]/div[3]/div/div/div[3]/div[11]/div/div[1]/div/div[1]/div[2]/span[1]/span/a
'''