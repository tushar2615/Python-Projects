n=int(input())
"""for i in range(1,n+1):
    print("Hello World",i)
    
for i in range(n+1,1,-1):
    for j in range(1,i):
        print("*",end="")
    print("\n",end="")
for i in range(1,n+1):
    for j in range(1,i):
        print("*",end="")
    print("\n",end="")"""
   
for i in range(n,0,-1):
    for j in range(1,i):
        print(end=" ")
    print("#")

for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    print("#")

for i in range(n,0,-1):
    for j in range(1,i):
        print(end=" ")
    print("#")
    
for i in range(1,n+1):
    for j in range(1,i):
        print(end=" ")
    print("#")