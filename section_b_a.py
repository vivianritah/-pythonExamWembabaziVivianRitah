def employeeBonus():

    run = 1

    while run == 1:

        salary =  int(input("Enter your salary amount: "))
        yearsOfService =  int(input("Enter your years of service: "))

        if yearsOfService > 4:

            netBonusAmount = int((0.08 * salary))
            
        elif yearsOfService == 3:

            netBonusAmount = int((0.05 * salary))
        else:

            netBonusAmount = 0

        netSalaryAmount= salary + netBonusAmount     

        print(f"Your net bonus amount is: {netBonusAmount:,} and your final pay is {netSalaryAmount:,}")    

        run = int(input("Press 1 to continue or any number to quit: "))

        if run !=1:
            break


employeeBonus()