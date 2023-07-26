# # class 정의
# class Person:
#     # 속성(변수)
#     blood_color = 'red'

#     #메서드
#     def __init__(self, name):  # 개발자가 직접호출 X , 패시브라 생각하면 되나?
#         self.name = name

#     def singing(self):
#         return f'{self.name}가 노래합니다'

# # 인스턴스 생성
# singer1 = Person('iu')
# singer2 = Person('BTS')

# # 메서드 호출 
# print(singer1.singing())
# print(singer2.singing())

# # class 변수 사용
# print(singer1.blood_color)
# print(singer2.blood_color)

# # 인스턴스.메서드()
# 'abc'.upper() # 데이터가 무언가를 해

# class Person:

#     # 생성자 함수
#     def __init__(self, name):
#         self.name = name # 

#     def hello(self):
#         print(f"안녕하세요 저는 {self.name}입니다.")

# p1 = Person("chanwoo")


# p1 = Person("chanwoo")
# print = (p1.name)

# p2 = Person("gildong")
# print = (p2.name)
# # # 클래스.메서드(인스턴스 자기자신) # 위 코드의 전개형
# # str.upper('abc') # 데이터를 인자로 받아

# p1.hello()

# class MyClass:
#     pass

#     def __str__(self):
#         return f"나는 Myclass다"
    
# c1 = MyClass()
# print(c1)

# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))

# class Calculator:
#     def __init__(self):
#         self.result = 0
    
#     def add(self, num):
#         self.result += num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))

# class Person:
#     blood_color = 'red'

#     def __init__(self, name):
#         self.name = name
    
#     def singing(self):
#         return f'{self.name}가 노래합니다.'
    
# # 인스턴스 생성
# singer1 = Person('iu')
# #메서드 호출
# print(singer1.singing())

# print(singer1.blood_color)
    
# class Shape:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h

#     def __gt__(self, other):
#         return self.w * self.h > other.w * other.h
    
#     def __eq__(self, other):
#         return self.w * self.h ==other.w * other.h

# s1 = Shape(3, 4)
# s2 = Shape(4, 5)
# print(s2>s1)

# class Foo:
#     def func1(fiei):  # 파이썬 메서드의 첫번째 인자로 항상 인스턴스가 전달됨
#         print("function 1")
#     def func2(self):
#         print(id(self))
#         print("function 2")


# f = Foo()
# f.func2()
# f.func1()


# class Person:
#     blood_color = 'red'

#     def __init__(self, name):
#         self.name = name
    
#     def singing(self):
#         return f'{self.name}가 노래합니다.'
    
# # 인스턴스 생성
# singer1 = Person('iu')
# #메서드 호출
# print(singer1.singing())

# print(singer1.blood_color)


# ## 인스턴스와 클래스 간의 이름 공간
# class Person:
#     name ='unknown'

#     def talk(self):
#         print(self.name)

# p1 = Person()
# p1.talk()

# p2 = Person()
# p2. talk()
# p2.name = 'Kim' ## instance 변수
# p2.talk()

# 클래스 변수의 활용 
# 몇 명인지 확인하고 싶다면?
# class Person:
#     count = 0
#     def __init__(self, name):
#         self.name =name
#         Person.count += 1
    
# person1 = Person('iu')
# person2 = Person('BTS')

# print(Person.count)

# class Circle():
#     pi = 3.14

#     def __init__(self, r):
#         self.r = r

# c1= Circle(5)
# c2 = Circle(10)

# # Circle.pi = 5
# c2.pi = 5
# print(Circle.pi)
# print(c1.pi)
# print(c2.pi)

# print('hello'.upper())
# print(str.upper('hello'))


## 클래스 매서드 예시
# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name =name
#         Person.count += 1
#     @classmethod
#     def number_of_population(cls):
#         print(f'인구수는 {cls.count}입니다.')

# person1 = Person('iu')
# person2 = Person('BTS')

# Person.number_of_population()

# class StringUtils:
#     @staticmethod
#     def reverse_string(string):
#         return string[::-1]
    
#     @staticmethod
#     def capitalize_string(string):
#         return string.capitalize()
    
# text = 'hello, world'

# reversed_text = StringUtils.reverse_string(text)
# print(reversed_text)

# capitalized_text = StringUtils.capitalize_string(text)
# print(capitalized_text)

# class Circle:
#     def __init__(self, r):
#         self.r = r
    
#     def area(self):
#         return 3.14 * self.r * self.r
    
#     def __str__(self):
#         return f'[원] radius: {self.r}'
    
# c1 = Circle(10)
# c2 = Circle(1)

# print(c1)
# print(c2)

def my_decorator(func):
    def wrapper():
        print('함수 실행 전')
        result = func()
        print('함수실행후')
        return result
    return wrapper

@my_decorator
def my_function():
    print('원본 함수 실행')
    
my_function()