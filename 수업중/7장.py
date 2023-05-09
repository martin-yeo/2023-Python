#### 스택 : 리스트 함수 중 append(), pop() 이용
#### 큐 : 리스트 함수 중 append(), pop(0) 이용

# word = input("Input a word: ")
# word_list = list(word)
# print(word)
# print(word_list)

# result = []
# for _ in range(len(word_list)):
#     result.append(word_list.pop(0))

# print(result)

#### 튜플
# t = ( 1, 3, 5, 7, 9)
# l = [ 1, 3, 5, 7, 9]

# for i in range(5):
#     print(f't[{i}] : ', t[i])
#     print(f'l[{i}] : ', l[i])

# print(t[::-2])

#### 세트
# l = [1,2,3,1,2,3,4,5,6,7,8,9,0,13,14,15,7]
# s1 = set(l)
# print(s1, "의 원소의 개수 :", len(s1))
# s2 = set([1,3,5,7,9,11])
# print(s2, "의 원소의 개수 :", len(s2))
# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)

# print(l)
# print(s)
# s.add(1)
# print(s)
# s.update([1,4,5,6,7])
# print(s)
# s.remove(3)
# print(s)
# s.discard(2)
# print(s)

#### 딕셔너리
# country_code = {'USA':1, 'S.Korea':82, 'China':86, 'Japan':81}
# country_code['German'] = 49
# print(country_code)

# for k, v in country_code.items():
#     print(f'key : {k},  value : {v}')

# print(country_code.keys())
# print(country_code.values())

# if 'S.Korea' in country_code.keys():
#     print('있다')
# else:
#     print('없다')

#### 데크 (deque)
from collections import deque

word = input("문자열을 입력하세요 : ")
d = deque(word)
print(d)
d.rotate(-2)
print(d)
print(d.pop())
print(d.pop())
# print(d.pop(0))
print(d.popleft())
print(d)
d.append('카')
d.append('타')
d.appendleft('하')
print(d)
rd = deque(reversed(d))
print(d)
print(rd)