# 조건문
# if 조건 :
#     조건이 참이면 할일
#     그 다음 할일
# else :
#     조건이 거짓이면 할일

# myAge = int( input('너의 나이는? '))

# if myAge < 30 :
#     print('클럽에 입장가능!!')
# else :
#     print('입장 불가능')
#     print('(죄송합니다)')

# a = 11
# b = 20

# print(a > b)
# print(a < b)
# print( not(a < b) )

# if -- elif -- else

# score = int( input('성적을 입력하세요 : '))

# if score >= 90:  grade = 'A'
# elif score >= 80:  grade = 'B'
# elif score >= 70:  grade = 'C'
# elif score >= 60:  grade = 'D'
# else: grade = 'F'

# print(grade)
   
"""
# 1. 태어난 연도 입력받기
# 2. 연도를 정수(int)로 변경
bYear = int( input('태어난 연도를 입력하세요: '))
# 3. 연도로 나이 계산
age = 2023 - bYear + 1
# print('나이는 ', age, '세 입니다', sep='')
print(f'{bYear}년에 태어난 당신의 나이는 {age}세 입니다')
# 4. 나이를 if--elif--else문으로 아래와 같이 구분
#   4-1. 20~26 대학생
#   4-2. 17~19 고등학생
#   4-3. 14~16 중학생
#   4-4.  8~13 초등학생
#   4-5. 그 외 경우, 학생아님
if age <= 26 and age >= 20 : status = '대학생'
elif age < 20 and age >=17 : status = '고등학생'
elif age < 17 and age >=14 : status = '중학생'
elif age < 14 and age >=8  : status = '초등학생'
else: status = '학생아님'
# 5. 학생신분 출력
print(f'현재 당신의 신분은 {status}입니다.')
"""

# for i in range(1, 10, 2):
#     print(i)

# for i in range(1, 10, 1):
#     print(f'3 곱하기 {i}은/는 {3*i}입니다')

# rainbow = ['빨', '주', '노', '초', '파', '남', '보']
# for item in rainbow:
#     print('좋아하는 색상이 나오면 Y를 입력하세요')
#     print(item)
#     yesORno = input('좋아하는 색상인가요(y/n)? ')
#     if yesORno == 'y' or yesORno == 'Y': break

# # 1. 원하는 단을 입력받기
# # 2. 단을 int로 변환
# # 3. for문으로 구구단 출력

# print('*---- 구구단 프로그램(v1.5) ----*')

# while True:
#     dan = int(input('몇단을 출력할까요(2~9)[0이면 종료]? '))
#     if dan == 0:
#         print('종료합니다')
#         break        
#     elif dan >= 2 and dan <= 9:
#         print(f'=== 구구단 {dan}단 ===')
#         for i in range(1, 10, 1):
#             print(f'{dan} x {i} = {dan*i}')
#     else:
#         print('잘못 입력하셨습니다!')

    

# sentence = 'I love you'
# reverse_sentence = ''

# for char in sentence:
#     reverse_sentence = char + reverse_sentence

# print(sentence)
# print(reverse_sentence)

# 실습 : 숫자 찾기 게임
# import random

# guess_number = random.randint(1, 100)
# users_input = int(input('숫자를 맞혀보세요(1~100) : '))

# while (users_input is not guess_number):
#     if users_input > guess_number:
#         print('Down')
#     else:
#         print('Up')
#     users_input = int(input('숫자를 맞혀보세요(1~100) : '))
# else:
#     print(f'정답입니다! 입력한 숫자는 {users_input}입니다')



#-------------------------------------------------
# Lab : 평균 구하기
#-------------------------------------------------

kor_score  = [  49,  80,  20, 100,  80]
math_score = [  43,  60,  85,  30,  90]
eng_score  = [  49,  82,  48,  50, 100]
midterm_score = [ kor_score, math_score, eng_score ]

student_score = [ 0, 0, 0, 0, 0]
i = 0
for subject in midterm_score: # 3과목을 반복
    for score in subject:     # 과목별 점수(5개)를 반복
        student_score[i] += score    # 학생별 점수 합계
        i += 1  
    i = 0
else:
    print(student_score)
    f = lambda x:x/3
    student_average = list(map(f, student_score))
    # a, b, c, d, e = student_score
    # student_average = [a/3, b/3, c/3, d/3, e/3]
    # student_average = []
    # for item in student_score:
    #     student_average.append(item/3)
    print(student_average)
