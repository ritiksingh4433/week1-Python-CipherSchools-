n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j),end=" ")
    print()


n=5
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()


for i in range(n):
    for j in range(n):
        print(n-i-1,end=" ")
    print()


for i in range(n):
    for j in range(n):
        print(n-j-1,end=" ")
    print()


for i in range(n):
    for j in range(n):
        print(max(max(i+1,j+1),max(n-j,n-i)),end=" ")
    print()
