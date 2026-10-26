#numbers 
"""numbers = [10,20,30,40]

for x in numbers:
    print(x)

for i in range(1, 6):
    print(i)"""

"""a=int(input())
b=int(input())
sum=a+b
diff=a-b
prod=a*b
print("All three values", sum, diff, prod)"""

"""a=int(input())
if a%2==0:
    print("It is Even")
elif a%3==0:
    print("It is odd")
elif a==0:
    print("Zero")"""

"""num = [4,7,2,9]
total_sum = 0
for i in num:
    total_sum += i
print(total_sum)"""

"""num = [12,5,27,9,18]
smallest = num[0]
for i in num:
    if i < smallest:
        smallest = i
print("Smallest : ", smallest)"""


num = [2,7,8,11,14,5]
count = 0
for i in num:
    if i % 2==0:
        count += i
print(count)
