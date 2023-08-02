# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def talk(self):
#         print(f'반갑습니다. {self.name}입니다.')


# s1 = Person('김학생', 23)
# s1.talk()

# p1 = Person('박교수', 59)
# p1.talk()



# 매서드 중복 정의
# class Person:
#     def __init__(self, name, age): #매개변수 name
#         self.name = name     # slef.name = instance name
#         self.age = age

#     def talk(self):
#         print(f'반갑습니다. {self.name}입니다.')


# # class Professor(Person):
# #     def __init__(self, name, age, department):
# #         self.name = name
# #         self.age = age
# #         self.department = department

# # class Professor(Person):
# #     def __init__(self, name, age, department):
# #         Person.__init__(self, name, age)
# #         self.department = department

# class Professor(Person):
#     def __init__(self, name, age, department):
#         # Person.__init__(self, name, age)
#         super().__init__(name, age) # 상속이 많아지고 부모 클래스가 많아질 때 유연하게 대처 가능
#         self.department = department

# class Student(Person):
#     def __init__(self, name, age, gpa):
#         super().__init__(name, age)
#         self.gpa = gpa

# p1 = Professor('박교수', 49, '컴공과')
# p1.talk()
     
# s1 = Student('김학생', 20, 3.5)
# s1.talk()



# --

# class Person:
    
#     def __init__(self, name):
#         self.name = name    
       
#     def greeting(self):
#         return f'안녕, {self.name}'


# class Mom(Person):
#     gene = 'XX'

#     def swim(self):
#         return '엄마가 수영'
    
#     def __init__(self, name):
#         super().__init__(name) # 이게 정석적인 코드이긴 함..
    

# class Dad(Person):
#     gene = 'XY'

#     def walk(self):
#         return '아빠가 걷기'


# class FirstChild(Mom,Dad):
#     dad_gene = Dad.gene
#     def __init__(self, name):
#         super().__init__(name)

#     def swim(self):
#         return '첫째가 수영'

#     def cry(self):
#         return '첫째가 응애'

# baby = FirstChild('아가')
# print(baby.cry())
# print(baby.swim())
# print(baby.walk())
# print(baby.gene)
# # print(baby.dad_gene)
# print(FirstChild.mro())


# # 예외 처리
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')

# try:
#     num=int(input('숫자입력:'))
# except ValueError:
#     print('숫자가 아닙니다.')

# try:
#     num = int(input('100으로 나눌 값을 입력해:'))
#     print(100/num)
# except ValueError:  # 추후 계층구조 염두하여 에러처리 설정해야함.
#     print('숫자를 입력하라고')
# # except (ValueError, ZeroDivisionError):
# #     print('제대로 입력해라')
#     print('숫자를 입력하라고')
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야?')
# except:
#     print('에러가 발생했어')


# try:
#     num = int(input('100으로 나눌 값을 입력해:'))
#     print(100/num)
# except BaseException:  # 추후 계층구조 염두하여 에러처리 설정해야함.
#     print('숫자를 입력하라고')
# # except (ValueError, ZeroDivisionError):
# #     print('제대로 입력해라')
#     print('숫자를 입력하라고')
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야?')
# except:
#     print('에러가 발생했어')

my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')


