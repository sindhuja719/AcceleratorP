l=[]
for i in range (7):
    exp=int(input(f"Enter the expense for day {i+1}: "))
    l.append(exp)
total=sum(l)
avg=total/7
print(f"Total expenses is {total}")
print(f"Average expenses is {avg}")
d={"Total":total,"Average":avg}
print(d)
low,hig=min(l),max(l)
print(f"Lowest is {low} , highest is {hig}")