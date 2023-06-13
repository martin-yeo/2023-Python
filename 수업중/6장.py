# rainbow = ['빨', '주', '노', '초', '파', '남', '보']
# print(rainbow[0], rainbow[4])
# print(rainbow[-1], rainbow[-5])
# print(rainbow[2:4])
# print(rainbow[::2])

# a = 'TEAM'
# b = 'LAB'
# print(a + ' of ' + b)
# print((a + ' ') * 2)
# if 'a' in a:
#     print(a)
# else:
#     print(b)

# textString = '''
# Yesterday all my troubles
# seemed so far away
# Now it looks as though
# they're here to stay
# Oh, I believe in yesterday
# Suddenly
# I'm not half the man I used to be
# There's a shadow hanging over me
# Oh, yesterday came suddenly
# Why she had to go
# I don't know, she wouldn't say
# I said something wrong
# now I long for yesterday
# Yesterday love was such an
# easy game to play
# Now I need a place to hide away
# Oh, I believe in yesterday.
# Why she had to go
# I don't know, She wouldn't say
# I said something wrong
# Now I long for yesterday
# Yesterday love was
# such an easy game to play
# Now I need a place to hide away
# Oh, I believe in yesterday
# '''

# print(len(textString))
# print(textString.count('yesterday'))
# print(textString.lower().count('yesterday'))
# tmpString = textString.split();
# changedString = ' '.join(tmpString)
# # changedString = textString.replace('\n', ' ')

# f = open('yesterday.txt', 'w')
# f.write(changedString)
# f.close()

print(1, 2, 3)
print('a' + 'b' + 'c' , 7, sep='')


# C언어 style
print('%d %d %d' %( 1, 2, 3))

print('{type1} {type2}'.format(type1='a', type2='b', type3='c'))

print('{:=^25}'.format('낱말 맞히기 게임 v1.1'))

a=b=c=1
print('%d %d %d' %( a, b, c))

print(f'{"낱말 맞히기 게임 v1.3":=^25}')
print(f'a: {a}\nb: {b}\nc: {c}\na+b+c: {a+b+c}\n3*a+7: {3*a +7}')


