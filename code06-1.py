## 하수


## 전역 - 스택의 초기화
# stack = [None, None, None, None, None]
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

## 메인
# PUSH
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack)

# Pop
data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)
data = stack[top]
stack[top] = None
top -= 1
print('팝 -->', data)

print(stack)

