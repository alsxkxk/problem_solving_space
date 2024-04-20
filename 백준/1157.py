import sys
input = sys.stdin.readline

word = input().rstrip()
word = word.upper()

if (len(word)==1):
    print(word)
    exit()
set_ = set([])

for w in word:
    set_.add(w)

if len(set_)==1:
    print(word[0])
    exit()

answer = []
for s in set_:
    answer.append([s, word.count(s)])
answer.sort(key=lambda x:x[1])

if answer[-1][1] == answer[-2][1]:print('?')
else:print(answer[-1][0])

# word = input().rstrip().upper()
# word_list = list(set(word))
# cnt = []
#
# for i in word_list:
#     count = word.count(i)
#     cnt.append(count)
#
# if cnt.count(max(cnt)) >= 2:
#     print('?')
# else:
#     print(word_list[cnt.index(max(cnt))])
