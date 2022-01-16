word = 'python'

print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])

print('#############################')
print(word[0:2])
print(word[:2])

print(word[2:])

print('#############################')
# パイソンは文字列に直接代入不可
word = 'J' + word[1:]
print(word[:])
n = len(word)
print(n)

