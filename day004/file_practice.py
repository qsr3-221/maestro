with open("line.txt", "w") as f:
    f.write("line1\n")
    f.write("line2\n")
with open("line.txt", "r") as f:
    line = f.read()
    print(line)