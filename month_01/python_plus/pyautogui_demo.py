"""
    PyAutoGUI——做职场高手,让所有GUI自动化,击败无聊的办公室重复性操作
        GUI:图形用户界面(Graphical User Interface)
            例如 办公软件,音乐播放器...
        作用：自动控制鼠标和键盘。
        文档：https://pyautogui.readthedocs.io/en/latest/install.html
"""
# 准备一个自动化工具
import pyautogui

# 显示鼠标位置(必须在命令行中运行)
# pyautogui.displayMousePosition()

# 使用自动化工具的移动功能
pyautogui.moveTo(43,283,2) # 移动到酷狗音乐
#
pyautogui.doubleClick()# 双击打开酷狗音乐
#
# pyautogui.moveTo(842,888,2) # 移动到播放按钮
#
pyautogui.sleep(5) # 睡眠两秒(等待酷狗打开)

button_play_box = pyautogui.locateOnScreen('play.png')
button_play_location = pyautogui.center(button_play_box)

pyautogui.moveTo(button_play_location.x,button_play_location.y,2)

pyautogui.click()# 单击播放按钮

pyautogui.hotkey('win', 'd')


# 截屏
# img = pyautogui.screenshot(region=(213, 795, 70, 70))
# img.save("play.png")
