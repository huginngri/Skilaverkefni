hstoll1 = int(input("Input the cost of the item in $: "))
hstoll2 = hstoll1
month = 1
totalintr = 0.0
if hstoll1<2500:
    if hstoll1 > 1000:
        while hstoll2 > 0:
                intrests = hstoll2 * 0.02
                payment = 50.0
                blunt = intrests + hstoll2
                
                if blunt > 50.0:
                    payment = 50.0
                    hstoll2 -= (payment - intrests)
                    
                else:
                    payment = hstoll2 + intrests
                    hstoll2 -= hstoll2
                totalintr += intrests
                print("Month:",month, "Payment:", round(payment, 2), "Interest paid:", round(intrests, 2), "Remaining debt:", round(hstoll2, 2))
            
                month += 1
    else:
        while hstoll2 > 0:
            intrests = hstoll2 * 0.015
            payment = 50.0
            blunt = intrests + hstoll2
            
            if blunt > 50.0:
                payment = 50.0
                hstoll2 -= (payment - intrests)
                
            else:
                payment = hstoll2 + intrests
                hstoll2 -= hstoll2
            totalintr += intrests

            print("Month:",month, "Payment:", round(payment, 2), "Interest paid:", round(intrests, 2), "Remaining debt:", round(hstoll2, 2))
            
            month += 1
else:
    print("The input is too large")

print("Number of months: ", month-1)
print("Total interest paid: ", round(totalintr,2))

   