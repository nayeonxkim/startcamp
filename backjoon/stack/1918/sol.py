import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cal = input()

    new_cal = ''
    stack = []
    for char in cal:
        if char not in '+-*/()':
            new_cal += char

        elif char in '+-':
            if stack:
                while stack[-1] in '+-*/':
                    new_cal += stack.pop()
            stack.append(char)

        elif char in '*/':
            if stack:
                while stack[-1] in '*/':
                    new_cal += stack.pop()
            stack.append(char)

        elif char == '(':
            stack.append(char)

        elif 
