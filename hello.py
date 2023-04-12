# import sys

# def solution(num1, num2):
  
#   answer = num1 / num2
   
#   return answer
 
# str = input("이름을 입력하세요 : ")
# print(str, solution(7, 2))

# list_1 = [[1, 2], [3], [4, 5]]
# a,b,c = list_1
# list_2 = a + b + c

# print(list_2)
# import random

# colors = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
# print(colors)
# # colors.sort(reverse=True)
# # print(colors)

# # print(random.sample('가나다라마바사아자차카타파하', 4))

# while True:
#   while True:
#     itr = int(input('구구단 몇단을 원하세요(2-9)? '))
#     if itr >= 2 and itr <= 9:
#       break
#     else:
#       print('잘못 입력하셨습니다!')
  
#   print(f'{itr}단을 출력합니다.')
#   for i in range(1, 10):
#     print(f'{itr} x {i} = {itr * i}')

# # for i in range(itr):
# #   random.shuffle(colors)
# #   print(colors)
# #   print(random.sample(colors, 3))
  


import pandas as pd
import numpy as np
data = pd.read_csv('중간시험점수.csv', encoding='cp949', index_col=0, header=0)

# print(data.head())
# print(data.mean('columns'))
# print(data.mean('index'))
# print(data.mean('index').mean())
# print(data.mean('columns').mean())

# print(data.sort_index(axis=0, ascending=False))

data2 = data.copy()

data.loc['합계'] = data.sum().round(0)
data.loc['평균'] = data.mean().round(1)
data2['과목합계'] = data.sum(axis=1).round(0)
data2['과목평균'] = data.mean(axis=1).round(1)

print(data.sort_values(axis=1, by='합계', ascending=[False]))
# print(data.sort_values(by=['합계',0], ascending=[False, False]))