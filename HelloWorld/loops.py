num = int(input("Digite el numero de escalones: "))
a = 1
for i in range(a,num+1):
    b = 0
    for j in range(b,i):
        print("*",end = ' ')
        b+=1
    print("")
    