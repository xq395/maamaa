import pyautogui
import time

print("=== 坐标获取工具 ===")
print("将鼠标移动到目标按钮上，按Ctrl+C复制坐标")
print("等待5秒开始...")
time.sleep(5)

try:
    while True:
        x, y = pyautogui.position()
        rgb = pyautogui.screenshot().getpixel((x, y))
        print(f"X: {x:<4}  Y: {y:<4} | RGB: {rgb} | 按Ctrl+C退出", end='\r')
except KeyboardInterrupt:
    print("\n坐标已捕获！")