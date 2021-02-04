import os
import random
import string
import time

import keyboard

os.startfile("notepad.exe")

barmaglot_verse = """Варкалось. Хливкие шорьки
Пырялись по наве,
И хрюкотали зелюки,
Как мюмзики в мове.

О бойся Бармаглота, сын!
Он так свирлеп и дик,
А в глуще рымит исполин -
Злопастный Брандашмыг.

Hо взял он меч, и взял он щит,
Высоких полон дум.
В глущобу путь его лежит
Под дерево Тумтум.

Он стал под дерево и ждет,
И вдруг граахнул гром -
Летит ужасный Бармаглот
И пылкает огнем!

Раз-два, раз-два! Горит трава,
Взы-взы - стрижает меч,
Ува! Ува! И голова
Барабардает с плеч.

О светозарный мальчик мой!
Ты победил в бою!
О храброславленный герой,
Хвалу тебе пою!

Варкалось. Хливкие шорьки
Пырялись по наве,
И хрюкотали зелюки,
Как мюмзики в мове.\n"""

new_string = """""".join(random.choices(string.ascii_uppercase + string.digits, k=10))
old_name = "".join(random.choices(string.ascii_uppercase + string.digits, k=7))

# saving original verse to a randomly generated txt file
time.sleep(3)
keyboard.write(barmaglot_verse)
keyboard.send("ctrl+s")
keyboard.write(f"{old_name}.txt")
keyboard.send("f4")

# replacing path with desktop
for i in range(40):
    keyboard.send("backspace")

time.sleep(0.5)
keyboard.write("Рабочий стол")

for i in range(4):
    keyboard.send("enter")

# writing new string into existing file
time.sleep(0.5)
keyboard.write(new_string)
keyboard.send("ctrl+shift+s")
keyboard.write(f"{old_name}_new.txt")
keyboard.send("enter")
keyboard.send("alt+f4")
