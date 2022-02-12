def computepay(h, r):
    if h > 40:
        return 40 * r + ((h - float(40)) * (r * 1.5))
    elif h <= 40:
        return h * r


hrs = float(input("Enter Hours:"))
rps = float(input("Enter Hours per Rate"))

p = computepay(hrs, rps)
print("Pay", p)
