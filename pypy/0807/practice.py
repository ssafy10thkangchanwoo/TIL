# s = 'reverse'
# s_lst = list(s)
# N = len(s)
# print(N)
# for i in range(N//2):
#     s_lst[i], s_lst[N-1-i] = s_lst[N-1-i], s_lst[i]
# s = ''.join(s_lst)
# print(s_lst)
# print(s)
#

# s1 = 'abc'
# s2 = 'abc'
# s5 = s1[:3]
# print(s1, s2, s5)
# if s1 == s2:
#     print('s1==s5')
# else:
#     print('s1 != s5')
# if s1 is s2:
#     print('s1 is s5')
# else:
#     print('s1 is not s5')

# s1 = 'aBc'
# s2 = 'Abc'
#
# print(s1 < s2)
# print(s1 > s2)
# print(s1 == s2)


# a = [1, 2, 3]
# # a = list(map(str, a))
# a = list(map(str, a))
# a = ''.join(list(map(str, a)))
#
# print(a)


# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x)-ord('0')
#     return i
#
# s = '123'
# a = atoi(s)
# print(a)


def itoa(a):
    s = ''
    while a>0:
        s += chr(ord('0') + a % 10) # 1의 자리 숫자 ASCII 코드 값
        a //= 10
    return s[::-1]

a= 123
print(itoa(123))