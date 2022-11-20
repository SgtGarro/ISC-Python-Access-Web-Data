name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dct = dict()
lst = list()

for line in handle:
    line = line.rstrip("\n")
    if not line.startswith("From "):
        continue
    words = line.split(" ")
    hour = words[6].split(":")[0]
    dct[hour] = dct.get(hour, 0) + 1

for k, v in dct.items():
    lst.append((k, v))

lst.sort()

for k, v in lst:
    print(k, v)