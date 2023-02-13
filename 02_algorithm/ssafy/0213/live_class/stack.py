stack = [0] * 3

# 가장 처음 top은 제일 마지막 위치
top = -1

# push 10
top += 1
stack[top] = 10

top += 1
stack[top] = 20

top += 1
stack[top] = 30

# pop
top -= 1
print(stack[top+1])