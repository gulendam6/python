soz = input("Sozu daxil edin: ")
soz2 = ''
for i in soz:
  if i not in soz2:
    soz2 =soz2+i
    print ("tekrarlar olmadan:",soz2)
