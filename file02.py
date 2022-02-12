# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sumValue = 0.0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count+1
        no = line.find("0")
        num = line[no:no+6]
        sumValue = sumValue + float(num)

print("Average spam confidence:",sumValue/count)
