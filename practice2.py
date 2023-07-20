for i in range(40):
    pass 
else:
    pass


# else문이 반복을 실행한 이후 실행됩니다.
# 반복문이 break문으로 종료될 때 else문이 실행되지 않음.
# break를 통해 중간에 종료되지 않은 경우에만 else문이 실행

# 반복문이 중간에 종료된 적이 있는지를 검사할 때 유용하게 사용

string1 = "apple"
string2 = "banana"
for c in string1:
    # apple 문자열을 순회하면서 알파벳 'b'가 있으면 b!를 출력한 다음 반복문을 종료.
    if c == 'b':
        print('b!')
        break
else: # for한번도 중단되지 않으면 실행되
    print("이 단어 안에는 b가 없습니다.")

    # else문은 중간에 break를 통해 종료되지 않을 때만 실행된다.

for num in range(1, 11):
    if num % 2 == 1:
        continue
    # else:
    print(num, end = " ")

for num in range(1, 11):
    if num % 2 == 1:
        pass
    
    print(num, end = " ")

# List comprehension dictionary
my_dict = {i: i**2 for i in range(10)}
print(my_dict)


scores = {'chanwoo' : 100, 'gildong':80, 'jaedong':70}

# 1. 기본적으로 key만 가져감
for name in scores:
    # print(name)
    # print(scores[name])
    print(f'{name}: {scores[name]} {scores.get(name)}')

# 2. 
for name in scores.keys():
    print(f'{name}: {scores[name]} {scores.get(name)}')

# 3.
for score in scores.values():
    print(score)

# 4.
for key, value in scores.items():
    print(f"{key} : {value}")