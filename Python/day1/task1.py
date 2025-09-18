students={}
for i in range(5):
    name=input(f"enter student name {i+1}: ")
    students[name]=int(input(f"enter marks of {name}:"))
l=list(students.values())
avg=sum(l)/len(students)
print("Average marks of the students:",avg)
highest=max(students,key=students.get)
print(f"Highest Scorer:{highest}",students[highest])
lowest=min(students,key=students.get)
print(f"Lowest scorer:{lowest}",students[lowest])

print("\nStudents with marks greater than 50:")
for n,m in students.items():
    if m>50:
        print(f"{n}->{m}")


