fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.rstrip("\n").split(" "):
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)