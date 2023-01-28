import xlwings


# # pip list => 설치된 패키지 리스트
# 가상환경 설정
# # python -m venv {가상환경이름}
# 가상환경 진입
# # myenv\Scripts\activate
# powershell 권한설정
# # Set-ExecutionPolicy RemoteSigned -> Y

# vs code 인터프리터 설정
# # python select interpreter -> 가상환경 선택

# 가상환경의 설치된 패키지 및 패키지 버전확인
## pip freeze
### pip freeze > requirements.txt -> text파일로 내보냄

# 가상환경 벗어날 때 
## teminal > deactivate

print(xlwings.__version__)