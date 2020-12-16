num = 0
tot = 0.0
while True:
    sval = input("enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except:
        print("Invaild input")
        continue
    num = num + 1 #counter
    tot = tot + fval #sum all input
    
print(tot,num,tot/num)