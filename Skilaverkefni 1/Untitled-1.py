hstoll = int(input("Input the cost of the item in $: "))
month = 1
if hstoll<2500:
    while hstoll > 0:
        if hstoll > 1000:
            intrests = hstoll * 0.02
            payment = 50.0
            hstoll -= payment - intrests
            
        elif hstoll <= 1000:
            intrests = hstoll * 0.015
            blunt = intrests + hstoll
            
            if blunt > 50.0:
                payment = 50.0
                hstoll -= (payment - intrests)
                
            else:
                payment = hstoll + intrests
                hstoll -= hstoll
                

        print("Month: ",month, " Payment: ", round(payment, 2), " Interest paid: ", round(intrests, 2), "Remaining debt: ", round(hstoll, 2))
        
        month += 1
else:
    print("The input is too large")
   