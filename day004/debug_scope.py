count = 0

def increase():
    global count
    count = count + 1
    print(count)

increase()
print(count)
def increase(count):
    count = count + 1
    return count

count = 0
count = increase(count)
print(count)