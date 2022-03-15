import random
from colorama import *
import time as t


main = 0
min = 0
may = 0
num = 0
sym = 0

t.sleep(1)
print(Fore.GREEN + """
██████████████████████████████████████████████████████████▀███████████████
█▄─▄▄─██▀▄─██─▄▄▄▄█─▄▄▄▄█▄─█▀▀▀█─▄█─▄▄─█▄─▄▄▀█▄─▄▄▀███─▄▄▄▄█▄─▄▄─█▄─▀█▄─▄█
██─▄▄▄██─▀─██▄▄▄▄─█▄▄▄▄─██─█─█─█─██─██─██─▄─▄██─██─███─██▄─██─▄█▀██─█▄▀─██
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀
""")

t.sleep(1)
print(Fore.RED + """
                                                    ░█▀▀█ █──█ 　 ░█─── ▀█▀ ░█─▄▀ 
                                                    ░█▀▀▄ █▄▄█ 　 ░█─── ░█─ ░█▀▄─ 
                                                    ░█▄▄█ ▄▄▄█ 　 ░█▄▄█ ▄█▄ ░█─░█
                                                    
                                                    
""")

t.sleep(1)
main = input(Fore.YELLOW + """
[1] Generar Contraseña Dificil
[2] Generar contraseña ExtraDificil
[3] Generar contraseña ExtraOrdinaria
    >_ """)


if main == "1":

    min = "aeiou"
    may = "AEIOU"
    num = "012345"
    sym = "!._#$%¡?¿/*°"
    str = min + may + num + sym 
    length = 14
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


elif main == "2":

    min = "qwertyuiopasdfghjklzxcvbnm"
    may = "QWERTYUIOPASDFGHJKLZXCVBNM"
    num = "0123456789"
    sym = "!¬#$%&/()=?¡¿++~*{[}]:-_<>"
    str = min + may + num + sym 
    length = 19
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


elif main == "3":

    min = "qwertyuiopasdfghjklñzxcvbnmãÇÈüï"
    may = "QWERTYUIOPASDFGHJKLÑZXCVBNMÃçèÜÏ"
    num = "0123456789ↀↁↈ"
    sym = "!¬#$%&/()=?¡¿++~*{[}]:-_<>❛❜❝❞"
    str = min + may + num + sym 
    length = 27
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


else:

    print(Fore.RED + "Ha ocurrido un error... Intenta solo con numeros del 1-3 sin espacios ni otras letras!")
    print(Fore.WHITE + "")
