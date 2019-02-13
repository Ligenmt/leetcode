"""
最长不重复子串长度
逐个记录，直到遇到重复的字母
"""

s = 'abcabc'
c = ''
length = 0
m = 0
for i in range(len(s)):
    if s[i] in c:
        if length > m:
            m = length
        c = c.split(s[i])[1]
        length = len(c)
    length += 1
    c += s[i]
if length > m:
    m = length
print(m)