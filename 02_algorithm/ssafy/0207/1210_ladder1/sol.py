'''
100 * 100 matrix

'''
import sys
sys.stdin =open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]


