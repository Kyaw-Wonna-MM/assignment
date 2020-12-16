# hrs = input("Enter Hours:")
# hr=0
# try:
#     hr = float(hrs)
# except:
#     hr=-1

# if hr > 0:
#     if hr >= 45:
#         rate = 10.50
#         Pay = hr * rate
#         print(Pay)
#     elif hr >= 40:
#         rate = 1.5
#         Pay = hr * rate
#         print(Pay)
#     else:
#         print("lower 40")
# else:
#     print("Value Error")


sh =input("enter hour: ")
sr =input("enter rate: ")
try:
    fh =float(sh)
    fr =float(sr)
except:
    print("ERROR!,input numeric")
    quit()
    
print(fh,fr)
gp = fh * fr

if fh > 40 :
    bonus=(fh-40)*(fr*0.5)
    Pay= gp + bonus
    print(Pay)
else:
    print(gp)

