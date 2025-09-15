

import pyautogui
import time
import pyperclip
import json

def leer_hologramas(path='holograma.json'):
    """Lee los hologramas desde un archivo JSON escalable."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                raise ValueError("El archivo JSON debe contener una lista de objetos.")
            return data
    except FileNotFoundError:
        print(f"Archivo {path} no encontrado.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error de formato en {path}: {e}")
        return []


def construir_comandos(holograma):
    """
    Construye los comandos de FancyHolograms usando un objeto holograma.
    El objeto debe tener al menos 'nombre' y 'text'.
    """
    nombre = holograma.get('nombre')
    texto = holograma.get('text')
    lore = holograma.get('lore')
    text2 = holograma.get('text2')
    text3 = holograma.get('text3')
    text4 = holograma.get('text4')
    text5 = holograma.get('text5')
    text6 = holograma.get('text6')
    text7 = holograma.get('text7')
    text8 = holograma.get('text8')
    text9 = holograma.get('text9')
    if not nombre or not texto:
        raise ValueError("Cada holograma debe tener 'nombre' y 'text'.")
    comandos = [
        f"/hologram create text {nombre}",
        f"/hologram edit {nombre} setline 1 {texto}",
        f"/hologram edit {nombre} scale 1.5",
        f"/hologram edit {nombre} background transparent",
        f"/hologram edit {nombre} textshadow true",
        f"/hologram edit {nombre} billboard VERTICAL",
        f"/hologram edit {nombre} rotatepitch 0",
        f"/hologram edit {nombre} visibility MANUAL",

        #-- Separador visual entre dos hologramas
        f"/hologram create text {lore}",

        #-- Comandos para el segundo holograma
        f"/hologram edit {lore} setline 1 {text2}",
        f"/hologram edit {lore} addline {text3}",
        f"/hologram edit {lore} addline {text4}",
        f"/hologram edit {lore} addline {text5}",

        #-- si necesitas más lineas en el holograma quita el comentario = #
        #f"/hologram edit {lore} addline {text6}",
        #f"/hologram edit {lore} addline {text7}",
        #f"/hologram edit {lore} addline {text8}",
        #f"/hologram edit {lore} addline {text9}",
        

        f"/hologram edit {lore} background transparent",
        f"/hologram edit {lore} textshadow true",
        f"/hologram edit {lore} billboard VERTICAL",
        f"/hologram edit {lore} rotatepitch 0",
        f"/hologram edit {lore} visibility MANUAL"
    ]
    return comandos

def enviar_comando(comando):
    #"""Abre el chat, escribe el comando y presiona Enter."""
    time.sleep(0.2)  # Pequeña pausa antes de abrir el chat
    pyautogui.press('t')
    time.sleep(0.4)  # Espera más para asegurar que el chat se abra
    pyperclip.copy(comando)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)  # Espera más para asegurar que el texto se pegue
    pyautogui.press('enter')
    time.sleep(0.4)  # Espera más para asegurar que el chat se cierre y el juego procese


def main():
    hologramas = leer_hologramas()
    if not hologramas:
        print("No se encontraron hologramas válidos en holograma.json.")
        return
    print(f"Se encontraron {len(hologramas)} holograma(s):")
    for i, holo in enumerate(hologramas, 1):
        print(f"  {i}: nombre={holo.get('nombre')!r}, text={holo.get('text')!r}")
    print("\nEn 4 segundos se comenzará el envío de comandos para todos los hologramas...")
    time.sleep(4)
    for holo in hologramas:
        try:
            comandos = construir_comandos(holo)
        except Exception as e:
            print(f"Error en holograma {holo}: {e}")
            continue
        print(f"\nComandos generados para '{holo.get('nombre')}':")
        for c in comandos:
            print(f"  {c}")
        for cmd in comandos:
            if not cmd.strip():
                print("Comando vacío, se omite.")
                continue
            print(f"Enviando: {cmd}")
            enviar_comando(cmd)
            time.sleep(0.5)

if __name__ == '__main__':
    try:
        import pyperclip
    except ImportError:
        print("pyperclip no está instalado. Instalando automáticamente...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'pyperclip'])
        import pyperclip
    main()
