#a)
print("a)")
for i in range (5):
    print(i)

#b)
print("b)")
for x in range(1,10,2):
    print(x)

#c)
print("c)")
for n in range(5,0,-1):
    print(n)

#d)
print("d)")
soma = 0
for i in range(0,10,5):
    soma += 1
    print(i)
    print(soma)

#e)
print("e)")
soma = 0 
for i in range(5,10):
    print(i)
    print(soma)

#f)
print("f)")
n = 100
for i in range(100,50,-10):
    sub = n-i
    print(i)
    print(sub)

#g)
print("g)")
soma = 0 
for i in range(10):
    if i == 3:
        continue
    if i == 7:
        break
    soma += 1
    print(i, soma) 