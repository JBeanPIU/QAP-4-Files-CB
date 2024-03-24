# The One Stop Insurance program, dedicated towards calculating new insurance policy information for our customers!
# By: Cameron Beanland
# Date: Mar 21st, 2024
 

# Library imports.
import datetime 
import FormatValues as fv
import os
import time
from sys import exit

 
# Define progarm constants.
POLICY_NUM    = 1944
BASIC_PREMIUM = 869.00
DISC_ADD_CAR  = 0.25
LIABILITY_COV = 130.00
GLASS_COV     = 86.00
LOAN_COV      = 58.00
TAX_RATE      = 0.15
MONTHLY_FEE   = 39.99
EXIT_COMMAND  = "EXIT"
currDate      = datetime.datetime.today()
allowedChars  = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,-' ")
allowedNums   = set("1234567890()-")
yesNo         = set("YyNn")


# Loop that the whole program takes place in.
while True:
    print()
    print("Enter all information requested. If you would like to exit, enter EXIT as the customer's first name")
    print()


    # Starting off by gathering user inputs!
    while True:
        custFirst   = input("Enter the customer's first name:                ")
        if not custFirst:
            print()
            print("Error - customers first name can not be left blank.")
            print()
            continue
        elif custFirst == EXIT_COMMAND:
            exit()
        else:
            custFirst = custFirst.title()
            break

    while True:
        custLast    = input("Enter the customer's last name:                 ").title()
        if not custLast:
            print()
            print("Error - customers last name can not be left blank.")
            print()
            continue
        else:
            custLast = custLast.title()
            break

    while True:
        addLine     = input("Enter the customer's address:                   ").title()
        if not addLine:
            print()
            print("Error - address line can not be left blank.")
            print()
            continue
        else:
            addLine = addLine.title()
            break
    
    while True:
        cityName    = input("Enter the name of the city:                     ").title()
        if not cityName:
            print()
            print("Error - city name can not be left blank.")
            print()
            continue
        else:
            cityName = cityName.title()
            break

    while True:
        provName    = input("Enter the province name [XX]:                   ").upper()
        if not provName:
            print()
            print("Error - province can not be left blank.")
            print()
            continue
        elif len(provName)!=2:
            print()
            print("Error - province name must be two letters only.")
            print()
            continue
        else:
            provName = provName.upper()
            break

    while True:
        postCode = input("Enter the postal code [X1X1X1]                  ").upper() 
        if not postCode:
            print()
            print("Error - postal code can not be left blank.")    
            print()
            continue   
        if len(postCode) != 6:
            print()
            print("Error - Postal code must have 6 characters.")  
            print()  
            continue
        if not (postCode[0].isalpha() and postCode[1].isdigit() and
            postCode[2].isalpha() and postCode[3].isdigit() and
            postCode[4].isalpha() and postCode[5].isdigit()):
            print("Error - invalid postal code format.")
            print() 
            continue  
        break

    while True:
     phoneNum = input("Enter the phone number [XXXXXXXXXXX]:           ")
     if  not phoneNum:
         print()
         print("Error - phone number can not be blank.")
         print()
     elif len(phoneNum) != 10:  
         print()
         print("Error - phone number must be 10 digits only.")
         print()
     elif phoneNum.isdigit() == False: 
         print()
         print("Error - phone number must be number digits only.")
         print()
         continue    
     else:
          break
     

    # Car related information! This includes number of cars insured, plus numerous benefits such as glass coverage or extra liability.    
    while True:
     numCarInsured = input("Enter the number of cars insured:               ")
     if not numCarInsured:
         print()
         print("Error - number of cars insured can not be left blank.")
         print()
         continue 
     numCarInsured = int(numCarInsured)
     if numCarInsured == 1:
         insurPremium = numCarInsured * BASIC_PREMIUM 
         break
     elif numCarInsured >= 2:
         exPremium = BASIC_PREMIUM * .75
         insurPremium = 869.00 + ((numCarInsured - 1) * exPremium)
         break
        
    while True:
     exLiability = input("Extra liability Y/N:                            ").upper()
     if not exLiability:
         print()
         print("Error - extra liability can not be left blank.")
         print()
         continue
     elif len(exLiability) !=1 or any(char not in yesNo for char in exLiability):
         print()
         print("Error - use only Y or N as values.")
         print()
         continue
     if exLiability == "Y":
         exLiability = LIABILITY_COV
     else: exLiability = 0.00
     break 
     
    while True:
     glassCov = input("Additional glass coverage? Y/N:                 ").upper()
     if not glassCov:
         print()
         print("Error - glass coverage can not be left blank.")
         print()
         continue
     elif len(glassCov) !=1 or any(char not in yesNo for char in glassCov):
         print()
         print("Error - use only Y or N as values.")
         print()
         continue
     if glassCov == "Y":
         glassCov = GLASS_COV
     else: glassCov = 0.00
     break      

    while True:
     loanCar = input("Add optional loaner car? Y/N:                   ").upper()
     if not loanCar:
         print()
         print("Error - loan car can not be left blank.")
         print()
         continue
     elif len(loanCar) !=1 or any(char not in yesNo for char in loanCar):
         print()
         print("Error - use only Y or N as values.")
         print()
         continue
     if loanCar == "Y":
         loanCar = LOAN_COV
     else: loanCar = 0.00
     break 
            

    # Calculations used to determine price of expenses       
    totalExtra     = loanCar + glassCov + exLiability
    totalInsurPrem = insurPremium + totalExtra
    taxes          = totalInsurPrem * TAX_RATE
    totalCost      = totalInsurPrem + taxes


    # Payment options, choose between full, monthly or down pay
    while True:
     payOptionType  = ["F", "M", "D"]
     downPayAmt = 0.00
     print()
     print             ("Options below are for full, monthly, and down pay respectively.")
     paySelect  = input("Enter payment method (F, M, D):                 ").title()
     if not paySelect:
         print()
         print("Error - payment method can not be left blank.")
         print()
         continue
     if paySelect in payOptionType:
         if paySelect == "F":
             payAmt = totalCost
             break
         elif paySelect == "M":
             payAmt = (totalCost + MONTHLY_FEE) / 8
             break
         elif paySelect == "D":
             payAmtAlt = input("Enter down pay amount:                          ")
             try:
                 downPayAmt = float(payAmtAlt)
                 payAmt = ((totalCost - downPayAmt) + MONTHLY_FEE) / 8
                 break
             except:
                 print()
                 print("Error - down payment amount must be a number.")
                 print()
     elif paySelect not in payOptionType:
         print()
         print("Error - must choose between 'full', 'monthly', or 'down pay.'")
         print()
         continue
     break
         

    claimNumList  = []
    claimDateList = []
    claimAmtList  = []


    while True:
     claimNum = input("Enter the claim number of recipient [##]:       ")
     if not claimNum:
         print()
         print("Error - claim number can not be left blank.")
         print()
         continue
     elif len(claimNum) !=2 or any(char not in allowedNums for char in claimNum):
         print()
         print("Error - claim number must be two digits only.")
         print()
         continue
     if claimNum == "00":
         print()
         print("Error - claim number can not be left at 00.")
         print()
     else:
         claimDate  = input("Enter the claim date (YYYY-MM-DD):              ")
         if not claimDate:
             print()
             print("Error - claim date can not be left blank.")
             print()
             continue
         claimAmt   = input("Enter the claim amount:                         ")
         if not claimAmt:
             print()
             print("Error - claim amount can not be left blank.")
             print()
         claimAmt   = float(claimAmt)
         claimNumList.append(claimNum)
         claimAmtList.append(claimAmt)
         claimDateList.append(claimDate)
         break
    

    # Invoice information
    invoiceDate = currDate.strftime("%d-%m-%Y")


    # Payment due dates
    if currDate.month == 12:
        payDate = datetime.date(currDate.year + 1,1,1)
        payDate = payDate.strftime("%d-%m-%Y")
    else:
        payDate = datetime.date(currDate.year, currDate.month +1,1)
        payDate = payDate.strftime("%d-%m-%Y")


    # Receipt results! Hopefully everything lines up well.
    print()
    print (f"--------------------------------")
    print (f"     The One-Stop Insurance     ")
    print (f"             Company            ")
    print (f"--------------------------------")
    print (f"Invoice date: {invoiceDate}     ")
    print (f"Policy #:     {POLICY_NUM}      ")
    print (f"                                ")
    print (f"Client Name & Address:          ")
    print (f"                                ")
    print (f"{custLast}, {custFirst:<12s}         ")
    print (f"{addLine:<25s}                       ")
    print (f"{cityName} {provName:<2s}, {postCode:<6s}          ")
    print (f"                                ")
    print (f"Phone Number: {phoneNum:<10s}        ")
    print (f"----------------                ")
    print (f"Cars insured:         {numCarInsured}     ")
    print (f"Extra liability:      {exLiability}       ")
    print (f"Glass coverage:       {glassCov}       ")
    print (f"Optional loan car:    {loanCar}       ")
    print (f"----------------                ")
    print (f"Extra costs:          {fv.FDollar2(totalExtra):>10s}")
    print (f"Insurance Premium:    {fv.FDollar2(totalInsurPrem):>10s}")
    print (f"HST:                  {fv.FDollar2(taxes):>10s}")
    print (f"----------------                ")
    print (f"Total cost:           {fv.FDollar2(totalCost):>10s}")
    print (f"Pay method:           {paySelect:>10s}")
    print (f"Down pay:             {fv.FDollar2(downPayAmt):>10s}")
    print (f"Total:                {fv.FDollar2(payAmt):>10s}")
    print (f"Payment date:         {payDate}")
    print (f"--------------------------------")
    print (f"       See you next time!       ")
    print (f"--------------------------------")


    # Claim information after receipt
    print ()
    print ()
    print (f"--------------------------------")
    print (f"Welcome to the claim's section. ")
    print (f"How many claims were done?")
    print (f"--------------------------------")
    if claimNum == 0:
     print(f"There are no previous claims.   ")
    else:
     print(f"Claim #  Claim Date       Amount")
    print (f"--------------------------------")
    print (f"{claimNum}       {claimDate}      {fv.FDollar2(claimAmt)}")
    print ()
    print (f"Saving data.", end='\r')
    time.sleep(0.7) 
    print ()
    print (f"Policy data has been saved!", end= '\r')
    print ()

    
    # Policy number now increased by one
    POLICY_NUM += 1
    

    # Housekeeping.
    while True:
        restart = input("Add another customer? Y/N:  ")
        if not restart:
            print()
            print("Error - cannot be left blank.")
            print()
            continue
        elif len(restart) != 1 or restart not in ['Y', 'y', 'N', 'n']:
            print()
            print("Error - use only Y or N as values.")
            print()
            continue
        if restart.upper() == "Y":
            break
        else: 
            print()
            print("Thanks for using the One-Stop Insurance Program!")
            print()
            break  
    if restart.upper() == "N":
        exit()
         



              
    