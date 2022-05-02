from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Edge()
driver.get("https://web.whatsapp.com")
print("Escaneie o QR code e logo após aperte enter")
input()
print("Logado")

contact = input("Para qual contato deseja enviar? (nome exato) ")
text = input("Qual o texto? ")
many = int(input("Quantas vezes enviar o texto? "))
type_mode = input("Modo flood (1) ou envio lento (2)? ")

inp_xpath_search = '//*[@id="side"]/div[1]/div/label/div/div[2]'
input_box_search = WebDriverWait(driver, 50).until(
    lambda driver: driver.find_element(By.XPATH, value=inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)

selected_contact = driver.find_element(
    By.XPATH, value="//span[@title='"+contact+"']")
selected_contact.click()

input_box_message = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
input_box = WebDriverWait(driver, 50).until(
    lambda driver: driver.find_element(By.XPATH, value=input_box_message))
i = 1
while i < many:
    if(type_mode == 2):
        time.sleep(2)
    input_box.send_keys(text + Keys.ENTER)
    if(type_mode == 2):
        time.sleep(2)
    print("Enviado " + str(i) + "/" + str(many))
    if (i > many):
        break
    i += 1
print("Todos enviados!")
driver.quit()
