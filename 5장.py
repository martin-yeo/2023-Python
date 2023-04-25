# def 함수이름(매개변수1, 매개변수2, ...):
#     명령문1
#     명령문2
#     ...
#     return <반환값>

# def calculate_rectangle_area(x, y):
#     answer = x * y
#     return answer

# rectangle_x = 10
# rectangle_y = 20
# print(f'사각형의 x의 길이 : {rectangle_x}')
# print(f'사각형의 y의 길이 : {rectangle_y}')

# area = calculate_rectangle_area(rectangle_x, rectangle_y)

# print(f'사각형의 넓이는 {area}입니다')

# def f(x):
#     return 2*x + 7

# def g(x):
#     return x**2

# # f = lambda x : 2*x + 7
# # g = lambda x : x**2

# x = int(input("x값을 입력: "))
# answer = f(x) + g(x) + f(g(x)) + g(f(x))

# print(f'정답은 {answer}입니다')

# def f(x):
#     y = x
#     x = 5
#     return y * y

# x = 3
# print(f(x))
# print(x)

# def f():
#     global s
#     s = "I love London!"
#     print(s)

# s = "I love Paris"
# f()
# print(s)
# # 팩토리얼을 구하는 재귀함수(자기 자신을 호출하는 함수, recursive function)
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# # 등차수열을 구하는 재귀함수 (a_1 = 1,   a_n = a_n-1 + 3)
# def adding(n):
#     if n == 1:
#         return 1
#     else:
#         return adding(n-1) + 3

# # 피보나치 수열을 구하는 재귀함수 (a_1 = 1, a_2 = 1, a_n = a_n-1 + a_n-2)
# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)

# num = int(input("수열 계산할 숫자 입력: "))
# print(f'팩토리얼({num}): {factorial(num)}')
# print(f'등차수열({num}): {adding(num)}')
# print(f'피보나치({num}): {fibo(num)}')

# def print_something(my_name, your_name='홍길동'):
#     print(f'안녕, {your_name}! 내 이름은 {my_name}이야')

# i = '여상수'
# you = '파이썬'
# print_something(i, you)
# print_something(your_name=you, my_name=i)
# print_something(i)

# rainbow = ['빨', '주', '노', '초', '파', '남', '보']
# print(rainbow)
# rainbow.sort(reverse=True)
# print(rainbow)

# print(5,7,9,10, sep='***')

# 가변 인수(매개변수) 0~무한대까지 여러개를 쓸수 있다
def test_asterisk(*args):
    a, b, *z = args
    print(a, b, z)
    return a + b + sum(z)


print(test_asterisk(1, 2, 3, 4))
