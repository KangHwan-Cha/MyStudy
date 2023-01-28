from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from tkinter import messagebox

# setting web driver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# first, quicksearch page is empty..not results
# get KS Std library
driver.get('https://quicksearch.dla.mil/qsSearch.aspx')
driver.find_element(By.XPATH, '//*[@id="GetFilteredButton"]').click()
with open('test.txt', 'w', encoding='UTF-8') as f:
    for _ in range(2242):
        time.sleep(2)
        element = driver.find_element(By.CSS_SELECTOR, '#GV > tbody')
        elements = element.find_elements(By.TAG_NAME, 'tr')
        cnt = 0
        for e in elements:
            rows = e.find_elements(By.TAG_NAME, 'td')
            extract = ''
            for row in rows:
                extract += row.text.replace(chr(10), "") + '|'
            if len(extract) > 5:
                cnt += 1
                f.write(f'{cnt} / {extract}\n')
        driver.find_element(By.XPATH, '//*[@id="btnNextEx"]').click()
        driver.implicitly_wait(5)
time.sleep(3)
driver.quit


# # show 50 list in page
# select=Select(driver.find_element(By.XPATH, '//*[@id="PageUnit"]'))
# select.select_by_visible_text("50개") # select visible text
# driver.find_element(By.CSS_SELECTOR, '#tabs-container > div.table.list > div > div > input').click()


# for i in range(13, 23):   # range(1, 23)   # iterable in Kind of KS
#     select=Select(driver.find_element(By.CSS_SELECTOR, '#s_codeClass'))
#     select.select_by_index(i) # select visible index
#     file_name = driver.find_element(By.CSS_SELECTOR, '#s_codeClass > option:nth-child({})'.format(i+1)).text
#     driver.find_element(By.CSS_SELECTOR, '#tab-1 > div > table > tbody > tr:nth-child(7) > td > div > input.ic_search01.small2.blue01').click()
#     now_break = False   # reset of breakpoint
#     with open('{}.txt'.format(file_name), 'w', encoding='UTF-8') as f:
#         while True:
#             for page in range(1, 11):   # range of page => 1, 11
#                 driver.find_element(By.CSS_SELECTOR, '#tabs-container > div.page > div > div > ul > li:nth-child({}) > a'.format(page+2)).click()
# <cut>
#                 curr_page, last_page = driver.find_element(By.CSS_SELECTOR, '#tabs-container > div.table.list > div > span:nth-child(2) > strong').text.split('/')
#                 if curr_page == last_page:   # 페이지 확인해서 중단점 설정
#                     now_break = True
#                     # messagebox.showinfo(message='Breakpoint')
#                     break
#             if now_break: break
#             try:
#                 driver.find_element(By.CSS_SELECTOR, '#tabs-container > div.page > div > div > ul > li.next > a').click()
#             except:
#                 messagebox.showerror("error","에러입니다.")

# time.sleep(5)

# print(chr(10))
# print('##### end #####')

# driver.get('https://www.naver.com/')
# time.sleep(2)
# driver.quit()

