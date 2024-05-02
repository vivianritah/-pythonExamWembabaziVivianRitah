import math



def valueOfD():
    
    X1 = int(input('Enter the value of X1:\t')) 
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) 
    Y2 = float(input('Enter the value of Y2:\t')) 

    formula = ((X1-X2) * (X1-X2)) + ((Y1-Y2) *(Y1-Y2))
    d = math.sqrt(formula)
  
    print("The value of d is: %.0f " %d + " ")

valueOfD()
