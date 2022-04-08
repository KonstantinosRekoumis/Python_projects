# ______________ PI SERIES FACTORS CALCULATOR _____________________
# Developed by Konstantinos Rekoumis, April 2022
# GitHub: https://github.com/KonstantinosRekoumis
#__________________________________________________________________
import math
print("#############################\n")
Pi = 3 #initialization value
N = 0 #counter
print("   Π approximation routine   \n")
n = int(input(" Please insert the number of your desired significant digits: \n"))
print("#############################\n")



_pi = f"{math.pi}"

# We check for the required factors to have n digits equality
# this is accomplished by converting pi to string and comparing it 
# to ground truth provided by math.pi
N = 0
while True:
    equality = True #initialization
    N  += 1
    Pi += (-1)**(N+1)*4/((2*N)*(2*N+1)*(2*N+2)) 
    
    _approx = f"{Pi}"
    #check for digits
    for i in range(n+2):
        if _approx[i] != _pi[i]: 
            equality = False
            break
    
    if equality:
        break
    



print("To approximate the π at ", n," digits, ", N," factors where required"   )
print(math.pi)
print(Pi)
print("\n#############################")