# result = list()
# for i in range(10):
#     result.append(i)
# print(result)

# result2 = [i for i in range(10)]
# print(result2)

# result3 = [i for i in range(10) if i % 2 == 0]
# print(result3)

# result4 = [i if i % 2 == 0 else '홀수' for i in range(10)]
# print(result4)

# result5 = [i if i % 3 != 0 else '짝' for i in range(1,10)]
# print(result5)

word1 = '갑을병정무기경신임계'
word2 = '자축인묘진사오미신유술해'
tenTwelve = [i+j for i in word1 for j in word2]
print(tenTwelve)