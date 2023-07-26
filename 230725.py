# # add
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)

# my_set.add(4)
# print(my_set)

# # clear
# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)    # set(),   빈중괄호{}는 dictionary로 됨.

# remove
# my_set = {1, 2, 3}
# my_set.remove(2)
# print(my_set)  

# print(my_set.remove(10))  # KeyError: 10

# discard
# my_set = {1, 2, 3}
# my_set.discard(2)
# print(my_set)  

# print(my_set.discard(10)) 
# # discard는 remove와 달리 없는 값을 삭제해도 에러없음, None 출력

# pop
# my_set = {1, 2, 3}
# element = my_set.pop()
# print(element)


# update(iteratble)
# my_set = {1, 2, 3}
# my_set.update = {4, 5, 1}
# print(my_set)


# set1 = {0, 1, 2, 3, 4}
# set2 = {1, 3, 5, 7, 39}
# set3 = {1, 4}
# print(set1.difference(set2))
# print(set1.intersection(set2))
# print(set1.issubset(set2))
# print(set3.isup)
# print(set1.union(set2))


### dictionary

# get(key[,default])
# person = {'name': 'Alice', 'age' : 25}
# print(person.get('name'))
# print(person.get('country')) #default값이 none
# print(person.get('country', 'Unknown'))

# print(person['name'])
# print(person['country']) # KeyError: 'country'

# #keys()
# person = {'name': 'Alice', 'age' : 25}
# print(person.keys())  # dict_keys(['name', 'age']), 리스트형으로 출력된다는 것이 관전포인트
# for key in person.keys():
#     print(key)

# #values()
# person = {'name': 'Alice', 'age' : 25}
# print(person.values())  # dict_keys(['name', 'age']), 리스트형으로 출력된다는 것이 관전포인트
# for value in person.values():
#     print(value)

# # items
# person = {'name': 'Alice', 'age' : 25}
# print(person.items())  #튜플형식으로 반환
# for key, value in person.items():
#     print(key, value)

# pop(key[,default])
# person = {'name': 'Alice', 'age' : 25}
# print(person.pop('age'))
# # print(person.pop('country')) # KeyError: 'country'
# print(person.pop('country', 'country 키는 없어요'))

# setdefault(key[,default])
# person = {'name': 'Alice', 'age' : 25}
# print(person.setdefault('age', '50'))
# print(person.setdefault('country', 'KOREA'))
# print(person)

# update([other])
# person = {'name': 'Alice', 'age' : 25}
# other_person = {'name': 'Jane', 'gender': 'Female'}

# person.update(other_person)
# print(person)

# person.update(age = 50)
# print(person)

# person.update(country = 'KOREA')
# print(person)


# # []
# # .get()
# # .setdefault()
# # 혈액형 인원수 세기
# # 결과 => {'A':3, 'B': 3, 'O': 3, 'AB': 3}
# blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# # []
# new_dict = {}
# for blood_type in blood_types:
#     # 기존에 키가 이미 존재 한다면,
#     if blood_type in new_dict:
#         #기존의 키 값을 +1 증가
#         new_dict[blood_type] += 1
#     #키가 존재하지 않는다면(처음 설정되는 키)
#     else:
#         new_dict[blood_type] = 1
# print(new_dict)    

# # get
# new_dict = {}
# for blood_type in blood_types:
    
#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1
    
# print(new_dict)    

# # setdefault
# new_dict = {}
# for blood_type in blood_types:
#     new_dict.setdefault(blood_type, 0)
#     new_dict[blood_type] += 1
        
# print(new_dict)    


# a= [1, 2, 3, 4]
# b = a
# b[0] = 100
# print(a)
# print(b)

# # 할당
# original_list = [1, 2, 3]
# copy_list = original_list
# print(original_list, copy_list)

# copy_list[0] = 'hi'
# print(original_list, copy_list)

#얕은복사
# 슬라이싱
# a = [1, 2, 3]
# b = a[:]
# b[0] = 100
# print(a, b)

# # copy
# c = a.copy()
# c[0] = 100
# print(a, c)

# # 얕은 복사의 한계
# a = [1, 2, [1, 2]]

# b = a[:]
# b[2][0] = 999
# print(a, b)

# c = a.copy()
# c[2][0] = 999
# print(a, c)

# 깊은 복사
import copy
original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)
deep_copied_list[2][0] = 999
print(original_list, deep_copied_list)