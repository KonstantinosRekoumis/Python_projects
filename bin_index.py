# ______________ BINARY INDEX CALCULATOR _____________________
# Developed by Konstantinos Rekoumis, April 2022
# GitHub: https://github.com/KonstantinosRekoumis
#_____________________________________________________________
#0,1,00,01,10,11,000

s = input("Give index :\n")

b = int(s,base=2) # convert to binary
l = len(s) #number of digits

if s == "1"*l: #full of Aces
    output = "0"*(l+1)
else:
    b +=  1 #increment index
    b = bin(b) #binary wizardry
    output = f"{b}"
    output = output[2:] # pop "0b"
    if len(output) != l: #supply the zeros in the front that are missing ie. (001->010), not (001->10)
        output = "0"*(l-len(output))+output

print(output)
