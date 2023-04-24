testString = '''
Yesterday all my troubles
seemed so far away
Now it looks as though
they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
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
Oh, I believe in yesterday
'''

f = open('yesterday.txt', 'r')
testString = f.readlines()
f.close()

testString = ''.join(testString) 
print(testString)
print(len(testString))
print(testString.count('yesterday'))
print(testString.count('Yesterday'))
print(testString.lower().count('yesterday'))
print(testString.replace('Yesterday', 'Tomorrow'))
print(testString.replace('\n', ' '))

print("{:=^50}".format("피라미드 출력"))

number = int(input("층수를 입력하세요:_____\b\b\b"))

for i in range(number):
    for j in range(number-i-1):
      print(" ", end='')
    for j in range(i):
      print("👍", end='')
    print()
    