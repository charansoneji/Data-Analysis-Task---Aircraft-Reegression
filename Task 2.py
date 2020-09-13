n = 5
print("Enter the number of times you want the pattern to repeat")
rep = int(input())
st = 0
for i in range(rep*4):
    if i%4 == 0:
        cnt = 1
        c = 0
        for j in range(c,n+2):
            if (i != 0 and j==0):
                cnt += 1
                continue
            else:
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
