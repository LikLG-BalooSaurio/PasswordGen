import random
from colorama import *
import time as t


print(Fore.GREEN + """
██████████████████████████████████████████████████████████▀███████████████
█▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─▄▄▀███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█
██─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─██─█─█─█─██─██─██─▄─▄██─██─███─██▄─██─▄█▀██─█▄▀─██
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀
""")

print(Fore.RED + """
                                                    ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                    ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                    ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
                                                    
                                                    
""")

min = "qwertyuiopasdfghjklñzxcvbnmãÇÈüï"
may = "QWERTYUIOPASDFGHJKLÑZXCVBNMÃçèÜÏ"
num = "0123456789"
sym = "!¬#$%&/()=?¡¿++~*{[}]:-_<>"


str = min + may + num + sym 
length = 25
password = "".join(random.sample(str,length))

t.sleep(2)

print(Fore.YELLOW + "Espera un momento, Se está creando tu contraseña!...")

t.sleep(4)


print(Fore.GREEN + """
    Tu contraseña es:

            """, Fore.YELLOW + password,
Fore.GREEN + """

    Vuelve a ejecutar si quieres una nueva contraseña! 
""")
