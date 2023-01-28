import csv
import os
import inspect
def csvToList_1(path):
    # csv 경로를 받아 리스트로 변경
    # 1차원일 경우에만 사용
    data_list = []

    f = open(path, encoding='utf-8')
    rea = csv.reader(f)
    for row in rea:
        data_list.append(row[0])
    f.close

    return data_list

if __name__ == '__main__':
    path = r'C:\Users\WINTEK1\Documents\Project\Programming\#Study\WEB Automation\Standardization\search_standard.csv'
    print(csvToList_1(path)) 