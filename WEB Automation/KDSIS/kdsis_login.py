from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time

# cmd Command: start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeTEMP"
# setting web driver

driver = webdriver.Chrome()
driver.implicitly_wait(5)

# get KS Std library
driver.get('https://vpn.dapa.go.kr/')
time.sleep(20)
# 수동으로 로그인
## id: 1298157778kckan  pw: wintek@1729
## id: 1298157778kckan  pw: wintek2010!

# 새창 핸들링
driver.execute_script('window.open("http://kdsis.dapa.go.kr:8888/index.do");')
time.sleep(1)
driver.switch_to.window(driver.window_handles[-1])  #새로 연 탭으로 이동

driver.find_element(By.CSS_SELECTOR, '#ibx_loginId').send_keys('1298157778kckan')
driver.find_element(By.CSS_SELECTOR, '#ibx_loginPw').send_keys('wintek2010!')
driver.find_element(By.CSS_SELECTOR, '#btn_login').click()

driver.find_element(By.CSS_SELECTOR, '#gen_topmenu_2_btn_menuLabel').click()   # 목록관리
driver.find_element(By.CSS_SELECTOR, '#trv_Menu_label_15').click()   # 검색
driver.find_element(By.CSS_SELECTOR, '#trv_Menu_label_18').click()   # 지정품명집 get-in

driver.find_element(By.CSS_SELECTOR, 'tabMain1_tab_tabs4_tabHTML').click()
driver.find_element(By.ID, 'wq_uuid_65').send_keys('40223')
driver.find_element(By.ID, 'btn_search').click()


element = driver.find_element(By.CSS_SELECTOR, '#ggr_dataListGun_body_tbody')
elements = element.find_elements(By.TAG_NAME, 'tr')
for e in elements:
    print(e.text)


