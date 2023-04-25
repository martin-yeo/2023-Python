#4
a = "3.5"
b = "1.5"
print(a + b)

#5
a = "1.5"
b = 4
print(a * b)

#6
a = '3'
b = float(a)
print(b ** int(a))

#7
a = 53
b = 10
print(a % b)

#8
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])

#9
a = [0, 1, 2, 3, 4]
print(a[::-1])

#10
num = [1, 2, 3, 4]
print(num * 2)

#11
import random as ra
print(ra.sample('가나다라마바사아자차카타파하', 4))

#12
colors = ['빨', '주', '노', '초', '파', '남', '보']
print(colors)
colors.sort(reverse=True)
print(colors)


#13
listA = ['Mokwon', 'University', 'is', 'an', 'academic',
				'institute', 'located', 'in',
        'Daejeon']
listB = []
for i in range(len(listA)):
    if i % 2 != 1:
        listB.append(listA[i])
print(listB)


#14
result = 0
for i in range(5, -5, -2):
    if i < -3:
        result += 1
    else: 
        result -= 1
print(result)

#15
def calcValue():
    x = 10
    print("Value:", x)
x = 20
calcValue()
print("Value:", x)

#16
word = 'cool'
print(f'|{word:*<14}|')
print(f'|{word:*^14}|')
print(f'|{word:*>14}|')

#17
# while True:
#     itr = int(input('구구단 몇단을 원하세요(2-9)? '))
#     if itr >= 2 and itr <= 9:
#         break
#     else:
#         print('잘못 입력하셨습니다!')

# print(f'{itr}단을 출력합니다.')
# for i in range(1, 10):
#     print(f'{itr} x {i} = {itr * i:2}')

# #18
tString = '''Yesterday all my troubles
seemed so far away
Now it looks as though
they're here to stay
Oh, I believe in yesterday
Suddenly I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go
I don't know, she wouldn't say
I said something wrong
now I long for yesterday
Yesterday love was such an
easy game to play
Now I need a place to hide away
Oh, I believe in yesterday.
Why she had to go
I don't know, She wouldn't say
I said something wrong
Now I long for yesterday
Yesterday love was
such an easy game to play
Now I need a place to hide away
Oh, I believe in yesterday'''

print(len('YESTERDAY') )
print(tString.count('yesterday'))
print(tString.count('Yesterday'))
print(tString.lower().count('yesterday'))
# print(tString.replace('\n', ' '))
c = tString.lower().replace('yesterday', 'tomorrow')
# print(c)
print(c.title().count('Y'))


#18
# a_1, a_2, a_3, ...
def facto(n=5):
    if n == 1: return 1
    else: return n * facto(n-1)

def iFacto(n=5):
    if n == 1 : return 1
    else:
        An = An_1 = 1
        for i in range(2, n+1):
            # An = i * An_1
            # An_1 = An
            An *= i
        return An

print(f'facto : {facto(7)}')
print(f'iFacto : {iFacto(8)}')

#19
def sunflowerTower(floor):
    for i in range(0, floor):
        print('🌻'*(i+1))
    for i in range(0, floor):
        print('🌻'*(floor-i-1))

print("{:=^40}".format("< Sunflower Tower >"))
floor = int(input('층수를 입력하세요(1~20): '))
sunflowerTower(floor)

