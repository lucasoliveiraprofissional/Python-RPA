# CRUD em .TXT
Scripts criados para conter vários registros de números de telefone.<br>
Um arquivo auxiliar .txt terá os registros de números de telefone e um script em Python fará operações com ele.<br>
O Script lerá todo o arquivo com a função 'with open'. Após ler todos os registros, entraremos em um laço while e um novo número só será adicionado se ele for único nesse
arquivo .txt, ou seja, esse arquivo só terá números não repetidos, a inserção só ocorre se já não existir um outro número igual ao número que está em processo de inserção.<br><br>
Este script e arquivo auxiliar será consumido por um script Python em Selenium Webdriver que fará scraping em grupos de Whatsapp e registrará os números contidos
nesses grupos. Haverão leves alterações e modificações futuramente.<br><br>
Um objetivo futuro é realizar as demais tarefas de um CRUD, ou seja, retornar um registro pesquisado e excluir um registro.
