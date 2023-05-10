text = '''A press release is the quickest 
and easiest way to get free publicity. 
If well written, a press release can result 
in multiple published articles about your firm and its products. 
And that can mean new prospects 
contacting you asking you to sell to them. ...'''

from collections import Counter

c =  Counter(text.lower().split())

for word, count in c.most_common():
  print(word, count)
