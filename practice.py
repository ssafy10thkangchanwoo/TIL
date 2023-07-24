## 주피터'y' 다시 코드모드로 변경
## 'm' 쉘 하나가 마크다운 모드로 변경
## 'a' 커서 기준 위에 쉘 하나 추가
## 'b' 커서 기준 아래 쉘 하나 추가
## 'dd' 쉘 삭제
## shift + enter : 실행 후 커서를 아래로 이동
## ctrl + enter  : 실행 후 커서를 제자리에

API_Key = '4e52d6f6bf95b01a68aa10206929ee02'

lat = 37.56
lon = 126.97
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}'

import requests
# API 요청 보내기
response = requests.get(url).json()
print(response)
