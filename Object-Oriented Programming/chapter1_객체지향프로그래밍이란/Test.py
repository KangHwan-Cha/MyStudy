from random import *

x = randint(1, 20)
y = uniform(0, 2)

print(x)
print(y)

x = 0.1
print(x >= 0)

"""
게임 캐릭터가 살아있으면 공격한 캐릭터의 공격력만큼 체력을 깎는 메소드
조건:
    1. 이미 캐릭터가 죽었으면 죽었다는 메시지를 출력한다
    2. 남은 체력보다 공격력이 더 크면 체력은 0이 된다.
"""