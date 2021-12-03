fich = open("input.txt","r")

sol=0
cont=0

for line in fich:
    value=int(line)
    if(cont==0):
        previous=value
    else: 
        if(value>previous):
            sol = sol + 1
        previous = value
    cont = cont + 1
    
print(f"Lines: {cont}")
print(f"Solution: {sol} ")

fich.close()