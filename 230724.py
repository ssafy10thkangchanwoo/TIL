# print('banana'.find('a')) # 인덱스1 반환
# print('banana'.find('z')) # 없어서 -1 반환 # -1을 활용가능
# print('banana'.index('a'))
# # print('banana'.index('z')) # ValueError: substring not found
#                             # 에러가 발생하면 코드 중단

# string1 = 'HELLO'
# string2 = 'Hello'

# print(string1.isupper())
# print(string2.isupper())
# print(string1.islower())
# print(string2.islower())
# print((string1+string2).istitle())


# string1= 'Hello'
# string2 = '123'
# print(string1.isalpha()) # 문자열이 알파벳으로만 이루어져 있는지 확인
# print(string2.isalpha())
# print((string1+string2).isalpha())

# text = 'hello, world! hello, world! hello, world!'
# new_text = text.replace('world', 'python', 2)
# print(new_text)
# text = '  hello, world!     ' 
# new_text = text.strip()
# print(text)
# print(new_text)

# text = '!hello, world!' 
# new_text = text.strip('!')
# print(text)
# print(new_text)

# text = 'hello, world' 
# words = text.split(',')
# print(words) 

# words = ['Hello', 'world!']
# text = '-'.join(words)
# print(text)

my_list = [1, 2, 3]
numbers = [4, 5, 6]
my_list.append([4, 5, 6])  
print(my_list.append(numbers))   #
print(my_list)

my_list = [1, 2, 3]
my_list.extend([4, 5, 6]) # [ ] 를 벗겨내고 기존 list 에 추가
print(my_list)


my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)

my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()    # i값 작성하면 i번째, 미작성시 제일 마지막 항목 제거
item2 = my_list.pop(0)

print(item1)
print(item2)
print(my_list)

# my_list = [1, 2, 3, 4, 5]
# my_list.clear()
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# index = my_list.index(2)
# print(index)  # 그 값이 아니라, 그 값의 인덱스를 반환

# my_list = [1, 3, 2, 3, 4, 3, 2, 5]
# count = my_list.count(3)
# print(count)

# my_list = [1, 2, 3] 
# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)

# my_list = [1, 2, 3, 5, 4] 
# # sort method
# # print(my_list.sort())
# # sorted 함수
# print(sorted(my_list))  # 원본 변경 안함, 
# print(my_list)



# numbers = [ 1, 2, 3]
# # 내일 복사/카피에 대한 내용에 대한 튜토리얼
# # 1. 할당
# list1 = numbers

# # 2. 슬라이싱
# list2 = numbers[:]

# numbers[0] = 100
# print(list1)
# print(list2)

# tuple_1 = (3, 4, 5, 6, 2, 1)  # tuple 변경 불가능..
# print(sorted(tuple_1))  # 리스트 됨. 복사본 생성
# print(tuple_1)

# string1 = "하다가"
# string2 = "zxcba"
# print(sorted(string1))
# print(sorted(string2))

# dic = {"c" : 3, "b" : 10, "a": 5} #  키를 기준으로
# print(sorted(dic))

# # ex) 딕셔너리를 정렬하고 싶은데 키가 아니라 값을 기준으로 정렬
# # "c", "a", "b"
# def sort_key(item):
#     # 정렬 기준을 return
#     print(item)
#     return item[1]


# print(sorted(dic.items(), key = sort_key)) # key 인자는 정렬방법을 서술할 함수

# print(sorted(dic.items(), key = lambda item: item[1]))
# # ex) 딕셔너리를 정렬하고 싶은데 키가 아니라 값을 기준으로 정렬
# # "c", "a", "b"