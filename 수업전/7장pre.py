#############################
# collections 실습
#############################
import collections as cl

# #############################
# # namedtuple
# #############################
# Point = cl.namedtuple('Point', ['x', 'y'])
# p = Point(11, 22)
# print(p)
# print(p.x, p.y)  # print(p[0] + p[1])
# x, y = p
# print(x, y)

#############################
# OrderedDict
#############################
nDict = dict()
nDict['x'] = 100
nDict['l'] = 500
nDict['y'] = 200
nDict['z'] = 300
print("nDict", nDict)

oDict = cl.OrderedDict();
oDict['x'] = 100
oDict['y'] = 200
oDict['z'] = 300
oDict['l'] = 500
print("oDict", oDict)

def sortKey(t):
  return t[0]

oDict2 = cl.OrderedDict(sorted(nDict.items(), key=lambda t: t[0]))
print("oDict2",oDict2)


#############################
# Counter
#############################
text1 = '''A press release is the quickest 
and easiest way to get free publicity. 
If well written, a press release can result 
in multiple published articles about your firm and its products. 
And that can mean new prospects 
contacting you asking you to sell to them. ...'''.lower().split()
print(text1)
counterText1 =  cl.Counter(text1)
print(counterText1)
for word, count in counterText1.most_common():
  if count >= 3:
    print(word, count)

text2 = '오늘 오후에는 오늘 오전보다 수업을 많이 하지 않습니다. 수업에서 중요한 것은 참여를 많이 하는 것입니다.'.split()
print(text2)
counterText2 = cl.Counter(text2)
print(counterText2)
for k, v in counterText2.most_common():
    if v >= 3:
        print(k, v)

counterText1a = cl.Counter("".join(text1))
print(counterText1a)
counterText2a = cl.Counter("".join(text2))
print(counterText2a)

for k, v in counterText1a.most_common():
    if v >= 20:
        print(k, v)
for k, v in counterText2a.most_common():
    if v >= 3:
        print(k, v)
