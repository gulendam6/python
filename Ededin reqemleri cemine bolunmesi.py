num = int(input("Ededi daxil edin: "));   

rem = sum = 0;    

n = num;    

 

while(num > 0):    

    rem = num%10;    

    sum = sum + rem;    

    num = num//10;    



if(n%sum == 0):    

    print("Beli, " + str(n) + " ededi " + str(sum) + "-a bolunur.");   

else:    

    print("Xeyr, " + str(n) + " ededi " + str(sum) + "-a bolunmur."); 
