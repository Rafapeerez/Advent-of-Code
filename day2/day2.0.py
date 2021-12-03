fich=open("/home/rafa/ASL/AoC/day2/input2.txt","r")

cont=0
position=0
depth=0
mult=0
vector = []

for lines in fich:
    vector.append(lines.split())
    cont+=1

for action, number in vector:
    if(action == "forward"):
        position = position + int(number)
    else : 
        if(action == "down"):
            depth = depth + int(number)
        else:
            if(action == "up"):
                depth = depth - int(number)

mult=position*depth

print(f"Position: {position}")
print(f"Depth: {depth}")


print(f"Lines: {cont}")
print(f"Solution: {mult}")

fich.close()