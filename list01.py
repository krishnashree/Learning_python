#file name - romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    n = line.split()
    for i in n:
        if len(lst)== 0 :
            lst.append(i)
        elif i not in lst :
            lst.append(i)
print(sorted(lst))
