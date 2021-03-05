n = int(input())
l = [0,1]
for i in range(2,1001): #assuming there are less than 1000 numbers that are prime factors of 2, 3 ,5
    if i%2==0 or i%3==0 or i%5==0:
        l.append(i)
print(l[n])