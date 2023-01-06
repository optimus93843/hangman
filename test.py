data = {}

with open ("data.txt") as f:
    for line in f:
        #print(line)
        (key, val) = line.split(",")
        data[key] = val[:-1]
print(data)

