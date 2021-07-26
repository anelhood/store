'''
    python自动化刷抖音
'''

from appium  import  webdriver
import  time

server = "http://localhost:4723/wd/hub"
param = {
	"platformVersion": "7.1.2",
	"platformName": "Android",
	"appPackage": "com.ss.android.ugc.aweme",
	"appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
	"deviceName": "127.0.0.1:62001"
}
# 启动这个软件
driver = webdriver.Remote(server,param)


# 自己写刷抖音
def get_size(self):
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	return(x,y)
def swipe_up(self,t):
	screen = self.get_size()
	self.driver.swipe(screen[341]*0.5,screen[908]*0.75,screen[341]*0.5,screen[341]*0.25,5000)
time.sleep(10)

time.sleep(5)
#点击同意
driver.find_element_by_id("com.ss.android.ugc.aweme:id/a-8").click()

while True:
    time.sleep(10)
    start_x = 350
    start_y = 800
    distance = 500
    driver.swipe(start_x,start_y,start_x,start_y-distance)























