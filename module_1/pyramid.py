height = int(input("What height should the pyramid be? "))

while not (0 < height <= 23):
        height = int(input("Please Input Valid height (<24)"))

for i in range(height):
    count = i+1
    for j in range(height-count):
        print(" ", end=" ")
    for j in range(count + 1):
        print("#",end=" ")
    print()
