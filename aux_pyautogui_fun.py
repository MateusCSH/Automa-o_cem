import pyautogui as py
import time


def reduzir():
            py.PAUSE = 2
            py.press('win')
            py.write('chrome')
            py.press('enter')

            btn_op = py.locateCenterOnScreen('btndrive.png')
            py.click(btn_op.x, btn_op.y)
            time.sleep(2)
            click_icon_drive = py.locateCenterOnScreen('click_driv.png')
            py.click(click_icon_drive.x, click_icon_drive.y)
            
            time.sleep(2)
            clica_ale = py.locateCenterOnScreen('clickale2.png')
            py.moveTo(clica_ale.x, clica_ale.y)
            py.click(clica_ale.x,clica_ale.y)
            
            py.press('tab')

            py.write('REGISTRO C',0.3)
            py.press('down')
            py.press('down')
            py.press('enter')

            time.sleep(2.5)

