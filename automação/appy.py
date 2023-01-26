import pyautogui
from time import sleep

# 1. clicar e digitar meu usúario
pyautogui.click(680,386, duration=0.2)
pyautogui.write("david")
# 2.clicar e editar minha senha
pyautogui.click(696,411, duration=0.2)
pyautogui.write('12345')
# 3.clicar em "entrar"
pyautogui.click(592,440, duration=0.2)
# 4.Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preço = linha.split(',')[2]
        # 1. clicar em digitar produtos
        pyautogui.click(407,376 ,duration = 0.2)
        pyautogui.write(produto)
        # 2. clicar em digitar quantidade
        pyautogui.click(411,393 ,duration = 0.2)
        pyautogui.write(quantidade)
        # 3. clicar em digitar preço
        pyautogui.click(413,428 ,duration = 0.2)
        pyautogui.write(preço)
        # 4. clicar em registrar
        pyautogui.click(324,579 ,duration= 0.2)
        sleep(1)

