import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    word = input()

    stack = []
    for char in word:
        if char == '(' or char == '{':
            stack.append(char)

        else:
            if stack[-1] == '('

    print(stack)