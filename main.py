import time
import pyautogui as pag
pag.FAILSAFE = False  # 为按下显示桌面按钮设置成False
pag.PAUSE = 0.5  # 增大缓冲时间，防止在点击前电脑未加载好

screenWidth, screenHeight = pag.size()  # 获取当前屏幕分辨率（打开华为电脑管家可能会改变屏幕分辨率和比例）
pag.moveTo(screenWidth - 1, screenHeight - 1, 0.5)
pag.click()  # 显示桌面，避免打开的窗口影响程序运行

if pag.locateOnScreen('appButton.png'):  # 判断图标是否在屏幕桌面上
    x, y = pag.center(pag.locateOnScreen('appButton.png'))  # 将图标所在位置的中心像素坐标记录为x, y
    pag.moveTo(x, y, 0.5)
    pag.doubleClick()
    time.sleep(3)  # 停止三秒等待程序加载
    if pag.locateOnScreen('myDevicesButton.png'):  # 当前未选中我的设备
        x, y = pag.center(pag.locateOnScreen('myDevicesButton.png'))
        pag.moveTo(x, y, 0.5)
        pag.click()
        if pag.locateOnScreen('padButton.png'):
            x, y = pag.center(pag.locateOnScreen('padButton.png'))
            pag.moveTo(x, y, 0.5)
            pag.click()
        else:
            exit()
    elif pag.locateOnScreen('myDevicesActiveButton.png'):  # 当前已选中我的设备
        if pag.locateOnScreen('padButton.png'):
            x, y = pag.center(pag.locateOnScreen('padButton.png'))
            pag.moveTo(x, y, 0.5)
            pag.click()
        else:
            exit()
    else:
        exit()
else:
    exit()

time.sleep(15)  # 暂停15秒等待连接
for i in range(3):  # 总共尝试3次
    if pag.locateOnScreen('failButton.png'):  # 如果连接失败
        x, y = pag.center(pag.locateOnScreen('failButton.png'))
        pag.moveTo(x, y, 0.5)
        pag.click()
        if pag.locateOnScreen('disconnectButton.png'):
            x, y = pag.center(pag.locateOnScreen('disconnectButton.png'))
            pag.moveTo(x, y, 0.5)
            pag.click()
            pag.moveTo(x - 200, y - 200, 0.5)  # 移开鼠标，避免影响下一步同一位置的按钮的识别
            if pag.locateOnScreen('reconnectButton.png'):  # 重新连接
                x, y = pag.center(pag.locateOnScreen('reconnectButton.png'))
                pag.moveTo(x, y, 0.5)
                pag.click()
                time.sleep(5)  # 暂停5秒，等待搜索平板
                if pag.locateOnScreen('padButton2.png'):  # 如果找到了
                    x, y = pag.center(pag.locateOnScreen('padButton2.png'))
                    pag.moveTo(x, y, 0.5)
                    pag.click()
                    time.sleep(10)  # 暂停10秒等待连接
