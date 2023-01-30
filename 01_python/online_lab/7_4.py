'''
1937년 Collatz란 사람에 의해 제기된 이 추측은, 
주어진 수가 1이 될때까지 다음 작업을 반복하면, 
모든 수를 1로 만들 수 있다는 추측이다. 
그 원리는 아래와 같다.

원리  
i.입력된 수가 짝수라면 2로 나눈다.  
ii.입력된 수가 홀수라면 3을 곱하고 1을 더한다.  
iii.결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.

예를 들어, 
입력된 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 된다.
위 작업을 몇 번이나 반복해야하는지 반환하는 함수 collatz()를 작성하시오 
(단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환하시오.)
'''

def collatz(number):
    if number == 1:
            print(-1)
    else:
        i = 0
        while i <= 500:
            if number % 2:
                number = number * 3 + 1
            else: 
                number = number / 2
            i += 1

            if i == 500:
                print(-1)
                break

            if number == 1:
                print(i)
                break


collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1
