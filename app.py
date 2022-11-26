# Passos manuais em sequencia, dps tornar cada passo um codigo python
# Quais são os passos manuais:
# 1- Navegar até o tiktok
import webbrowser, pyautogui
from time import sleep
webbrowser.open('https://www.tiktok.com/')
sleep(4)
# 2- Clicar em login
pyautogui.click(1242,184, duration=2)
sleep(1)
# 3- Clicar em login com google
pyautogui.click(1026,540, duration=2)
sleep(4)
# 4- Clicar na minha conta
pyautogui.click(992,420, duration=2)
sleep(7)
# 5- Navegar até a pagina - https://www.tiktok.com/@guibarretobaixo
pyautogui.click(1187,134, duration=2)
pyautogui.press('delete')
sleep(1)
pyautogui.write('https://www.tiktok.com/@guibarretobaixo')
sleep(2)
pyautogui.press('enter')
sleep(6)
# 6- Clicar na postagem mais recente
pyautogui.click(913,605, duration=2)
sleep(5)
# 7- Verificar se video ja foi curtido
for video in range(15):   
    imagemcurtida = pyautogui.locateOnScreen('curtida.png')
    imagemnotcurtida = pyautogui.locateOnScreen('notcurtida.png')
    if imagemcurtida:
        #- Se foi curtido passar para o proximo video
        pyautogui.press('down')
        sleep(4)
    else:
        #- Se não foi curtido, curtir e passae para o proximo video
        pyautogui.click(imagemnotcurtida)
        sleep(4)




