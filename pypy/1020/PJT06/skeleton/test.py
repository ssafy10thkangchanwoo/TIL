# 핵심로직을 구현한 함수
# 회원에게만 제공하고 싶어

islogined= True
def check_login():
    if islogined:
        return True

def my_decorator(func):
    def wrapper():
        # 전처리
        if not islogined:
            print('로그인 하고 와라')
            return 

        func()
        print('로직끝남')
    return wrapper


@my_decorator
def myfunc():
    print('myfunc')

myfunc()
# 전처리, 후처리 로직이 너무 길다. -> 파이썬 데코레이터 이용



# def myFunc1():
#     # 로그인 되어 있는지 여부를 확인
#     check_login()
#     check_login()
#     check_login()
#     check_login()

#     print('myfunc')

    
#     # 로직이 끝났다. <안내문 제공>

# def myFunc2():
#     # 로그인 되어 있는지 여부를 확인
#     check_login()
#     print('myfunc')

#     # 로직이 끝났다. <안내문 제공>


# def myFunc3():
#     # 로그인 되어 있는지 여부를 확인
#     check_login()
#     print('myfunc')

#     # 로직이 끝났다. <안내문 제공>
# print(myFunc3)

