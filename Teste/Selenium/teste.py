from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # Importe a classe By

# Inicializar o driver do Selenium
driver = webdriver.Chrome()

# Abrir a página de teste
driver.get("file://Teste/Selenium/pagina_teste.html")  # Substitua "caminho/para" pelo caminho real

# Localizar os campos de usuário e senha
username_field = driver.find_element(By.ID, "username")  # Use a classe By.ID
password_field = driver.find_element(By.ID, "password")  # Use a classe By.ID

# Preencher os campos de usuário e senha
username_field.send_keys("seu_nome_de_usuario")
password_field.send_keys("sua_senha")

# Enviar o formulário
password_field.send_keys(Keys.RETURN)

# Verificar o resultado
assert "Página de sucesso" in driver.page_source

# Fechar o navegador
driver.quit()
