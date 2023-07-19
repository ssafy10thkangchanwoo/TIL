# import requests
# url = "https://random-data-api.com/api/v2/users"
# response = requests.get(url).json()

# print(response)

num = 10
def myfunc():
    global num
    num = 20 
    print("함수 실행: num을 20으로 바꿨다.")
    print(num)
myfunc()

print(num)

# filter(fucntion, iterable)
# 리스트의 홀수만을 걸러내는 함수
# function의 결과는 True of False 라는 점.
# 결과가 True인 것만 골라서 반환

def odd(n):
    return n % 2 

numbers = [1, 2, 3, 4, 5]
# new_numbers = list(filter(odd,numbers))
new_numbers = list(filter(lambda n: n % 2, numbers))
print(new_numbers)