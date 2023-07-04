import tkinter as tk
import subprocess

def execute_command():
    command = entry.get()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output_text.insert(tk.END, f">>> {command}\n{result.stdout}\n{result.stderr}\n")

def clear_output():
    output_text.delete("1.0", tk.END)

# Cria a janela principal
window = tk.Tk()
window.title("Interface")

# Cria o campo de entrada
entry = tk.Entry(window)
entry.pack()

# Cria o botão para executar o comando
execute_button = tk.Button(window, text="Executar", command=execute_command)
execute_button.pack()

# Cria o botão para limpar a saída
clear_button = tk.Button(window, text="Limpar", command=clear_output)
clear_button.pack()

# Cria o campo para exibir a saída
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Inicia o loop principal da interface
window.mainloop()