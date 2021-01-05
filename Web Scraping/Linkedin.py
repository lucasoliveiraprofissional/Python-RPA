from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from pyautogui import hotkey, typewrite, press, scroll
import pyperclip

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.get('https://www.linkedin.com//')

user = 'lucas.oliveira.profissional@hotmail.com'
pwd = ''
users, urls =[], []
filtro = str('') #Empresa que queremos filtrar os funcionários

loginx = '//*[@id="session_key"]' #LOGAR
login = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, loginx)))
login.send_keys(user)

senhax = '//*[@id="session_password"]' #DIGITAR SENHA
senha =  browser.find_element_by_xpath(senhax)
senha.send_keys(pwd)

entrarx = '/html/body/main/section[1]/div[2]/form/button' #CLICAR PARA ENTRAR
entrar =  browser.find_element_by_xpath(entrarx)
entrar.click()

buscax = '//*[@id="ember20"]/input' #NA HOME, PROCURAR CAMPO DE BUSCA
busca = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, buscax)))
busca.send_keys(" ") 
busca.send_keys(Keys.RETURN)

chatx = '//*[@id="msg-overlay"]/div[1]/header' #Minimizar o chat, fica encobrindo a visão da busca
chat = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, chatx)))
chat.click()

empresax = "//span[text()='Empresas atuais']" #NA PARTE DE BUSCA, CLICAR EM TODOS OS FILTROS
empresa = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, empresax)))
empresa.click()

press('tab') #Nessa parte aqui eu teria que obter o Xpath do campo de busca, farei isso no futuro.
typewrite(filtro)
sleep(2) #Nessa parte aqui eu teria que obter o Xpath da primeira empresa filtrada.
press('down')
press('enter')
press('tab')
press('enter')

try:
  for i in range(1,76): #76 no caso é o número de páginas que minha busca retornou, melhorarei isso no futuro
    sleep(5)            #fazendo com que o bot encontre o número da última página, o transforme em int e coloque dentro do for
    scroll(-500)
    sleep(3)
    scroll(-500)
    sleep(3)
    pessoas = browser.find_elements_by_xpath('//a[contains(@id,"ember")]//span[@class="name actor-name"]')
    for indice in pessoas:
      users.append(indice.text)#     nomes
    links = browser.find_elements_by_xpath("//a[contains(@data-control-name,'search_srp_result')]")
    for indice in links:
      urls.append(indice.get_attribute('href'))#     links
    avancarx = '//button[contains(@aria-label,"Avançar")]'
    avancar = browser.find_element_by_xpath(avancarx)
    avancar.click()
except Exception as erro:
  print(f'A causa do erro foi: {erro.__cause__}\nA classe do erro foi: {erro.__class__}\nO contexto do erro foi: {erro.__context__}')
finally:
  print('terminou')
  with open('users.txt', 'a', encoding='utf8') as f:
    for pessoa in users:
      f.write(f'{pessoa}\n')
  with open('links.txt', 'a', encoding='utf8') as f:
    for url in urls:
      f.write(f'{url}\n')