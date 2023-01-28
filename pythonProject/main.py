import collections
import re


def is_palindrome(s: str) -> bool:
    # 자료형 데크로 선언
    strs = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    print(strs)
    while len(strs) > 1:
        # print(strs[0], strs[-1])
        if strs.popleft() != strs.pop():
            return False

    return True


print(is_palindrome('racecar'))

s = 'sdfasdf;asdfAAAAasdf::::가나다;asdfasdf'
print(re.sub('[^A-Za-z0-9ㄱ-홓]', '', s), end='zzzzz')
re.sub