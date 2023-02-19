'''the purpose of this program is to calculate the home power consumption for individuals by prompting users
for their kwh usage at different times throughout the day
Created by: William Zhang, CS1026A'''
#set the price per kwh throughout the day and tax percent
offPeak = 0.085
peak = 0.176
midPeak = 0.119
tax = 0.13
#set a while loop that will continue to run until a 0 is entered
done = False
while not done:
    offPeakKWH = float(input("Enter kwh during Off Peak period: "))
    #if the offPeakKWH is 0, set done to true and end the program
    if offPeakKWH == 0:
        done = True
    else:
        #get the user to input all of the kwh used during each period
        PeakKWH = float(input("Enter kwh during On Peak period: "))
        midPeakKWH = float(input("Enter kwh during Mid Peak period: "))
        #ask if the user is a senior
        senior = (input("Is owner senior? (Y,y,N,n): "))
        #calculate the total prices for each kwh along with its corresponding period fee
        totalOff = offPeakKWH * offPeak
        totalPeak = PeakKWH * peak
        totalMid = midPeakKWH * midPeak
        #calculate the total cost by adding up all of the individual totals
        totalKWH = offPeakKWH + midPeakKWH + PeakKWH
        totalPrice = float(totalOff+totalPeak+totalMid)
        #if the total is less than 400kwh then give the user a 4% discount
        if totalKWH < 400:
            totalPrice = totalPrice - totalPrice*0.04
        #the total must be greater than 400kwh as it means the initial discount is not given
        #the peakKWH must also be less than 150. If these parameters are met, give the user a 5% discount
        elif totalKWH > 400 and PeakKWH < 150:
            #calculate the new total Peak price and add it to the total price
            totalPrice -= totalPeak
            totalPeak = totalPeak - totalPeak*0.05
            totalPrice += totalPeak
        #if the user is a senior and enters 'Y', or 'y', give the user an 11% discount
        #if the user is not a senior, do not change the total price
        if senior == "Y" or senior == "y":
            totalPrice = totalPrice - totalPrice*0.11
        #calculate the final price with tax included
        finalPrice = totalPrice*(1+tax)
        #print out the final price
        print("Electricity cost:", "$%.2f" %(finalPrice))
        #extra space for next set of kwh inputs
        print("")
