#print electricity bill
# Less than 500 - 0.2 per unit
#  500 - 1000 - 0.4 per unit above 499 units
#  1001 - 1500 - 0.6 per unit above 1000 units
#  1501 - 2000 - 1.5 per unit above 1500 units
#  2001 and above - 2.5 per unit above 2000 units
def electricitybill():
    units=int(input("enter the bill"))
    if units <= 500:
        bill = units * 0.2
    elif units <= 1000:
        bill = (500 * 0.2) + (units - 500) * 0.4
    elif units <= 1500:
        bill = (500 * 0.2) + (500 * 0.4) + (units - 1000) * 0.6
    elif units <= 2000:
        bill = (500 * 0.2) + (500 * 0.4) + (500 * 0.6) + (units - 1500) * 1.5
    else:
        bill = (500 * 0.2) + (500 * 0.4) + (500 * 0.6) + (500 * 1.5) + (units - 2000) * 2.5
    print(f"Total bill for {units} units is ₹{bill:.2f}")

electricitybill()
