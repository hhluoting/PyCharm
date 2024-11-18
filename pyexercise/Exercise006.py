from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# 配置 ChromeDriver 路径，替换为你的 ChromeDriver 路径，你也可以将chromedriver拖入文件根目录，使用'./chromedriver.exe'路径。
chrome_driver_path = 'F:/ProgramData/anaconda3/envs/luoting/Scripts/chromedriver.exe'  # 替换为你的 ChromeDriver 路径

# 初始化 ChromeDriver Service
service = Service(chrome_driver_path)
# 打开浏览器时的相关配置，可以根据需求进行打开和关闭
options = Options()
options.add_argument("--start-maximized")  # 启动时最大化窗口
# options.add_argument("--disable-blink-features=AutomationControlled")  # 使浏览器不显示自动化控制的信息
# options.add_argument("--disable-gpu")  # 禁用GPU硬件加速
# options.add_argument("--disable-infobars")  # 隐藏信息栏
# options.add_argument("--disable-extensions")  # 禁用所有扩展程序
# options.add_argument("--disable-popup-blocking")  # 禁用弹出窗口拦截
# options.add_argument("--incognito")  # 启动无痕模式
# options.add_argument("--no-sandbox")  # 关闭沙盒模式（提高性能）
# options.add_argument("--disable-dev-shm-usage")  # 使用/dev/shm分区以避免共享内存问题
# options.add_argument("--remote-debugging-port=9222")  # 启用远程调试端口
# 初始化 WebDriver，并传入 ChromeDriver Service
driver = webdriver.Chrome(service=service, options=options)

# 打开百度搜索首页
driver.get("https://www.baidu.com")

# 打印页面标题
print(driver.title)
# 延时5秒钟，也就是浏览器打开5秒钟，避免闪退
time.sleep(5)
# 关闭 WebDriver
driver.quit()