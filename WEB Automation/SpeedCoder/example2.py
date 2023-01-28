# IHS.com
import time
from selenium import webdriver
from openpyxl import Workbook
from CsvToList import csvToList_1
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Workbook 생성
wb = Workbook(write_only=False)
ws = wb.create_sheet('Std_List')
ws.append(['규격번호', '활성상태', '대체규격'])

# 웹 드라이버 설정
##driver = webdriver.Chrome('C:\\Users\\star2\\Documents\\Cha_Project\\CodeIt\\웹페이지자동화\\chromedriver')
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# 찾으려는 규격
csv_path = r'C:\Users\WINTEK1\Documents\Project\Programming\#Study\WEB Automation\Standardization\search_standard.csv'
find_std = csvToList_1(csv_path)

# IHS Setting
driver.get('https://global.ihs.com/?rid=IHS')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '#onetrust-accept-btn-handler').click()
# 담아놓을 리스트 생성
Results = []

for i in range(len(find_std)):
    time.sleep(round(random.uniform(1, 5)))
    driver.get('https://global.ihs.com/search_res.cfm?&rid=IHS&input_doc_number={}&input_doc_title='.format(find_std[i]))
    time.sleep(1)
    for result_row in driver.find_elements(By.CSS_SELECTOR, 'div.divTableCell.valign-top.doc-data-column'):
        Name_Std = result_row.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span > a').text
        State_Std = result_row.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div:nth-child(1) > span:nth-child(2)').text
        if State_Std == 'Superseded By:':
            try:
                Replace_Std = result_row.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div:nth-child(1) > span:nth-child(3) > a').text
            except:
                Replace_Std = ''
        else:
            Replace_Std = ''
        ws.append([Name_Std, State_Std, Replace_Std])

        # 변수 초기화
        Name_Std = ""
        State_Std = ""
        Replace_Std = ""

time.sleep(5)
driver.quit()
wb.save('검색결과.xlsx')
wb.close()