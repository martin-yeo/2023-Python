# list comprehension : for + if
result = [i for i in range(10) if i % 2 == 0]
print(result)

result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

word_1 = "Hello"
word_2 = "World"
result = [i + j for i in word_1 for j in word_2]   
print(result)

word_1 = "갑을병정무기경신임계"
word_2 = "자축인묘진사오미신유술해"
result = [i + j for i in word_1 for j in word_2]   
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(), w.lower(), len(w)] for w in words] 
print(stuff)