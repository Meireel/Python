import math

jArray=[4.2, 0.3, 1.7]
m=7
c=2.1
r=4*10**-4

for j in jArray:
    h = (10 * r - j) / (c ** 2 + math.e ** -m)
    y = (h * m - j ** 2) + (0.1*c) ** 2
    print(h)
    print(y)

print(' ')
jArray=[0,0.1, 1.7]
i=0
while i<len(jArray):
    h = (10 * r - jArray[i]) / (c ** 2 + math.e ** -m)
    y = (h * m - jArray[i] ** 2) + (0.1 * c) ** 2
    print(h)
    print(y)
    i+=1

print(' ')
jArray=[9,1.8, 15, -3]
mArray=[1, 0.5, 2]
for j in jArray:
    for m in mArray:
        h = (10 * r - j) / (c ** 2 + math.e ** -m)
        y = (h * m - j ** 2) + (0.1 * c) ** 2
        print(h)
        print(y)
        print(' ')