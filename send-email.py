import pyperclip
import pyautogui
import time
import pandas as pd

# Pausa a cada ação do script
pyautogui.PAUSE = 1

# Endereço da tabela baixada
tabela = pd.read_csv(r"C:\Users\mtsfs\Documents\Programação\Python-Mail\produtos.csv", sep=";")
# Exibe a tabela
print(tabela)

# Faz as somas das colunas
total_gasto = tabela["ValorFinal"].sum()
quantidade = tabela["Quantidade"].sum()
# Cálculo do preço médio
preco_medio = int(total_gasto) / int(quantidade)

print("Total Gasto:", total_gasto)
print("Quantidade:", quantidade)
print("Preço Médio:", preco_medio)

# Abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Delay para a página carregar
time.sleep(3)

# Abrindo nova guia e abrindo o email
pyautogui.hotkey("ctrl", "t")
pyautogui.write("https://mail.google.com/mail/u/0/?ogbl#inbox")
pyautogui.press("enter")

# Delay para a página carregar
time.sleep(3)

# Clica no botão "Escrever"
pyautogui.click(x=80, y=169)
# Escrever o destinatário
pyautogui.write("mtsf.salvador@gmail.com")
# Confirma o destinatário
pyautogui.press("tab")

# Passar para o campo "Assunto"
pyautogui.press("tab")
# Escrever o assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

# Passar para o corpo do email
pyautogui.press("tab")
# Escrever o corpo do email
texto = f"""
Prezados,

Segue o relatório de compras.

Total gasto: {total_gasto:,.2f}
Quantidade de produtos: {quantidade:,}
Preço médio: {preco_medio:,.2f}

Estou à disposição para quaisquer dúvidas.

Atenciosamente,
Marco Túlio Salvador Filho
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# Enviar o email
pyautogui.hotkey("ctrl", "enter")