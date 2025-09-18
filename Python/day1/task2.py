s="Python is great for DevOps"
l=s.split(" ")
print(f"Number of words in {s} are {len(l)}")
print("\n",l)
l.reverse()
s1=""
for i in range (len(l)):
    s1+=l[i]+" "
print(s1)
l1=s.split(" ")
t=[(w,len(w)) for w in l1]
print(t)
