age=int(input("quelle age ?"))

if age < 12:
    print("gratuit")

elif age < 17:
    print("10chf")
    
elif age < 25:
    print("coute 25chf")
    
elif age < 65:
    print("coute 30chf")
    
else:
    print("coute 15chf")
    

