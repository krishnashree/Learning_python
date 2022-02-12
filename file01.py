# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for lines in fh:
    lines = lines.rstrip('\n')
    print(lines.upper())
