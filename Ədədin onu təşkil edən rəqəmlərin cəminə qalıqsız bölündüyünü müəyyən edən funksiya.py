def bolunen(a):
    b = 0
    for i in str(a):
        i = int(i)
        b += i
        
    if int(a) % b == 0:
        print(str(a) + " ədədi " + str(b) + " ədədinə bölünür.")
        
bolunen(133)
