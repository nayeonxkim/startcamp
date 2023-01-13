fc, vc, p = map(int,input().split())
if (p -vc) == 0: 
    print("다시 입력하세요.")
else:
    q = fc/(p-vc)
    if q < 0:
        be_point = -1
    else:
        be_point = int(q) + 1

    print(be_point)