# 실습 번호.py
number_of_people = 0
def increase_user(name):
    number_of_people +=1
    print(f'{name}님 환영합니다!')
     

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {}
    user_info["name"] = name
    user_info["age"] = age
    user_info["address"] = address
    return user_info


many_user = list(map(create_user, name, age, address))