def FeeCalc(dist, rate):
    fee = dist * rate
    fee_output = "₱" + str(fee)
    return fee_output

dist_input = float(input("Enter the total distance traveled in kilometers: "))
rate_input = float(input("Enter the rate of fuel per kilometer: "))
total_fee = FeeCalc(dist_input, rate_input)
print("Total delivery fee:", total_fee)