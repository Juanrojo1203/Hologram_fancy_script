
import pyautogui
import time
import pyperclip

def leer_argumentos(path='holograma.txt'):
    """Lee los argumentos desde un archivo externo, uno por línea."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Archivo {path} no encontrado.")
        return []

def construir_comandos(args):
    """
    Construye los comandos de FancyHolograms usando los argumentos dados.
    Se espera el siguiente orden en el archivo:
    1. nombre
    2. texto
    3. x
    4. y
    5. z
    6. jugador1
    7. jugador2
    """
    if len(args) < 7:
        raise ValueError("El archivo holograma.txt debe tener al menos 7 líneas: nombre, texto, x, y, z, jugador1, jugador2.")
    nombre, texto, x, y, z, jugador1, jugador2 = args[:7]
    comandos = [
        f"/fancyholograms create {nombre}",
        f"/fancyholograms settext {nombre} {texto}",
        f"/fancyholograms teleport {nombre} {x} {y} {z}",
        f"/fancyholograms showto {nombre} {jugador1}",
        f"/fancyholograms hidefrom {nombre} {jugador2}",
    ]
    return comandos

def enviar_comando(comando):
    """Abre el chat, escribe el comando y presiona Enter."""
    pyautogui.press('t')
    time.sleep(0.7)  # Espera más para asegurar que el chat se abra
    pyperclip.copy(comando)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.3)  # Espera más para asegurar que el texto se pegue
    pyautogui.press('enter')
    time.sleep(0.5)  # Espera más para asegurar que el chat se cierre y el juego procese

def main():
    argumentos = leer_argumentos()
    print("Argumentos leídos:")
    for i, arg in enumerate(argumentos, 1):
        print(f"  {i}: {arg!r}")
    if len(argumentos) < 7:
        print("Por favor, completa al menos 7 líneas en holograma.txt: nombre, texto, x, y, z, jugador1, jugador2")
        return
    comandos = construir_comandos(argumentos)
    print("\nComandos generados:")
    for c in comandos:
        print(f"  {c}")
    print("\nEn 4 segundos se comenzará el envío de comandos...")
    time.sleep(4)
    for cmd in comandos:
        if not cmd.strip():
            print("Comando vacío, se omite.")
            continue
        print(f"Enviando: {cmd}")
        enviar_comando(cmd)
        # Espera extra entre comandos para máxima seguridad
        time.sleep(1.5)

if __name__ == '__main__':
    try:
        import pyperclip
    except ImportError:
        print("pyperclip no está instalado. Instalando automáticamente...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'pyperclip'])
        import pyperclip
    main()
