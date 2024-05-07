# 1. Abrir o sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login


# para instalar a biblioteca: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar a tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab)

# Abrir o navegador (Chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# 2. Abrir o sistema da empresa 
pyautogui.click(x=897, y=385)
pyautogui.write("thiellen.oliveira95@gmail.com")

pyautogui.press("tab") # passou para o campo senha
pyautogui.write("Sua senha")

pyautogui.press("tab") # passou para o botão Login
pyautogui.press("enter")

time.sleep(3)

# 3. Abrir e importar a base de dados para cadastrar

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    # 4. Cadastrar um produto
    codigo = str(tabela.loc[linha, "codigo"])

    # Clicar no campo do código do produto
    pyautogui.click(x=785, y=255)

    # Preencher o código
    pyautogui.write(str(codigo))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher a marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher o custo 11.0
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Preencher a observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    # Passar para o próximo campo
    pyautogui.press("tab")

    # Apertar o botao
    pyautogui.press("enter")
    pyautogui.scroll(5000)