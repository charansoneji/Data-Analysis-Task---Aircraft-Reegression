n = 5
for i in range(n-1):
    if i%4 == 0:
        cnt = 1
        for j in range(n+2):
            print(cnt*' ',end='')
            print((n+2-cnt)*'| ',end='')
            print(cnt*'+ ',end='')
            print((n+2-cnt)*'| ',end='')
            print()
            cnt += 1
    if i%4 == 1:
        cnt = 6
        for j in range(n+2):
            print(cnt*' ',end='')
            print((n+2-cnt)*'- ',end='')
            print(cnt*'+ ',end='')
            print((n+2-cnt)*'- ',end='')
            print()
            cnt -= 1
    if i%4 == 2:
        cnt = 1
        for j in range(n+2):
            print(cnt*' ',end='')
            print((n+2-cnt)*'- ',end='')
            print(cnt*'+ ',end='')
            print((n+2-cnt)*'- ',end='')
            print()
            cnt += 1
    if i%4 == 3:
        cnt = 6
        for j in range(n+1):
            print(cnt*' ',end='')
            print((n+2-cnt)*'| ',end='')
            print(cnt*'+ ',end='')
            print((n+2-cnt)*'| ',end='')
            print()
            cnt -= 1
