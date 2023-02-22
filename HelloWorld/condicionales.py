ageA = int(input("Digite edad 1: "))
ageB = int(input("Digite edad 2: "))
ageC = int(input("Digite edad 3: "))

if ageA>ageB:
    if ageB>ageC:
        print (f"The ages from oldest to youngest are: {ageA} {ageB} {ageC}")
    else:
        if ageA>ageC:
            print (f"The ages from oldest to youngest are: {ageA} {ageC} {ageB}")
        else:
            print (f"The ages from oldest to youngest are: {ageC} {ageA} {ageB}")
else:
    if ageA>ageC:
        print (f"The ages from oldest to youngest are: {ageB} {ageA} {ageC}")
    else:
        if ageB>ageC:
            print(f"The ages from oldest to youngest are: {ageB} {ageC} {ageA}")
        else: 
            print(f"The ages from oldest to youngest are: {ageC} {ageB} {ageA}")