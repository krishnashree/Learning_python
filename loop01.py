largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        number = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = number
    if largest < number:
        largest = number
    if smallest is None:
        smallest = number
    if smallest > number:
        smallest = number

print("Maximum is", str(largest))
print("Minimum is", str(smallest))
