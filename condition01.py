hrs = input("Enter Hours:")
h = float(hrs)
ratePerHour = input("Enter rate per hours:")
rph = float(ratePerHour)
grossPay = float(0)
if h < 40:
    grossPay = h * rph
elif h > 40:
    grossPay = 40 * rph
    grossPay = grossPay + ((h - float(40)) * (rph * 1.5))
print(grossPay)
