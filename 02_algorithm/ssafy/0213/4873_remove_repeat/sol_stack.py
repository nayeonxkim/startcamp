import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    word = input()

    stack = []

    for char in word:
        if not stack:
            stack.append(char)
        elif stack and char != stack[-1]:
            stack.append(char)
        elif stack and char == stack[-1]:
            stack.pop()

    # 반대로
    for char in word:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    print(stack)