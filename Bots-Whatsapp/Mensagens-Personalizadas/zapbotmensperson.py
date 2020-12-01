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

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.maximize_window()

browser.get('https://web.whatsapp.com/')

with open('groups.txt', 'r', encoding='utf8') as f:
  groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
  msgs = [msg.strip() for msg in f.readlines()]


for group, msg in zip(groups, msgs):
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
  #(Atualmente consegui sucesso clicando na foto do usuário)
  group_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[1]/div/div/span'
  group_title = browser.find_element_by_xpath(group_xpath)

  sleep(1)

  #Clicar no resultado da busca
  group_title.click()

  sleep(1)

  #Achar o campo de texto pra digitar a mensagem
  input_xpath = '//div[contains(@class,"copyable-text selectable-text")]'
  input_box = browser.find_elements_by_xpath(input_xpath)

  pyperclip.copy(msg)

  input_box[1].send_keys(Keys.CONTROL + "v")
  sleep(2)
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
#browser.quit()


'''
  Estou usando o XPATH do nome do grupo/contato

  XPATH antigo:
  '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span'

  XPATH do conteudo todo, foto, nome, ultima mensagem etc...:
  //*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div[2]

  XPATH foto:
  //*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[1]/div/div/span
'''