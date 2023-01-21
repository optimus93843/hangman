data = {}
with open ("data.txt") as f:
    for line in f:
    
        (key, val) = line.split(",")
        data[key] = val[:-1]

print(data)

