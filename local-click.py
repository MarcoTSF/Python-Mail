import keyboard
from pynput import mouse

def on_click(x, y, button, pressed):
    global is_pressed_function_enabled

    if pressed and is_pressed_function_enabled:
        print(f"Clicou na posição ({x}, {y})")

def start_mouse_listener():
    global is_pressed_function_enabled
    is_pressed_function_enabled = False

    # Cria um listener para os eventos de clique do mouse
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    while True:
        if keyboard.is_pressed('j'):
            is_pressed_function_enabled = not is_pressed_function_enabled
            if is_pressed_function_enabled:
                print("Função pressed ativada.")
            else:
                print("Função pressed desativada.")

            # Aguarda a tecla "j" ser liberada antes de alternar novamente
            keyboard.wait('j', suppress=True)

# Chama a função para iniciar o listener do mouse
start_mouse_listener()