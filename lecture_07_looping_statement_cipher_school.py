# whilw loop

a=1
while a<10:
    print(a)
    a+=1

name="jatin"
name.__iter__
print(type(name))
print("***")
for c in name:
    print(c)
    print(type(c))

a=range(5)
print(a)

# break,continue,pass 

for i in range(5):
    print(i)
    if i==3:
        break

for i in [0,1,2,3,4]:
    print(i)
    i=100
    print(i)

for i in range(5):
    print(i)
    if i==3:
        break
else:
    print("something")