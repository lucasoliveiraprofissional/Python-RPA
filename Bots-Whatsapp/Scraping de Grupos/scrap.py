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

for group in groups:
  search_path = '//div[contains(@class,"copyable-text selectable-text")]'
  search_box = WebDriverWait(browser, 20).until(
  EC.presence_of_element_located((By.XPATH, search_path))
  )
  search_box.clear()
  pyperclip.copy(group)
  search_box.send_keys(Keys.CONTROL + "v")
  sleep(2)

  #Achar o caminho onde está o contato/grupo
  #(Atualmente consegui sucesso clicando na foto do usuário)
  #Clicando no título do grupo: //*[@id="pane-side"]/div[1]/div/div/div[12]/div/div/div[2]/div[1]/div[1]/span
  group_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[1]/div/div/span'
  group_title = browser.find_element_by_xpath(group_xpath)

  sleep(1)
  group_title.click()
  sleep(4)

  #Obter numeros listados no topo do grupo
  cabecalho_xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
  cabecalho_numeros = browser.find_element_by_xpath(cabecalho_xpath)
  numeros = cabecalho_numeros.text
  print(f'\n\nNúmeros: {numeros}')
  
  with open('contatos.txt', 'a', encoding='utf8') as f:
    f.write(f'\n{numeros.strip()}')

  sleep(3)

'''
#Desconectar da sessão aberta no Whatsapp Web:
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

'''
Estou usando o XPATH do nome do grupo/contato

XPATH antigo:
'//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span'

XPATH do conteudo todo, foto, nome, ultima mensagem etc...:
//*[@id="pane-side"]/div[1]/div/div/div[9]/div/div/div[2]

XPATH foto:
//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[1]/div/div/span

Mapeamentos de Xpath ainda não testados:
(Desse modo eu clicaria no nome do grupo dentro da conversa, depois
em "Mais participantes", ou na quantidade de participantes e os
mapearia na janela que abrisse)

numeros:
//*[@id="main"]/header/div[2]/div[2]/span

nome do grupo dentro do grupo:
//*[@id="main"]/header/div[2]/div[1]/div/span

Participantes:
//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[1]/div/div/div[1]/span

participante 1:
//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div/span/span

mais participantes:
//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[5]/div[2]/div/div

todos os participantes não add:
//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[5]/div[4]/div/div[7]/div/div/div[2]/div[1]/div[1]/span/span
'''
