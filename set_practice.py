"""
m=set()
print(type(m))
m.add(11)
print(m)
....................................................
ps:vowels:
s="hello worlds of egg and idli"
v=set()
c=0
for i in s:
    if i=='a'or i=='e' or i=='i' or i=='o'or i=='u':

        print("vowel is",i)
        v.add(i)
        c=c+1
print(v)
print("total vowels found",c)
..........................
ps:common element
s1=input("enter 1st string")
s2=input("enter 2nd string")
s3=list(set(s1)&set(s2))
for i in s3:
    print(i)
print(set(s3))

.......................................
s1={"apple","banana","chickoo"}
s2={"apricot","apple","orange","chickoo"}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1)
print(s1.difference_update(s2))
print(s1)
print(s1.update({"sadiya","bilal",1,2}))
print(s1)
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
print(s1)
.......................................................
m={1,2,3,44,55,69}
m2={1,2,55,69,4,8}
print(m^m2)

print(m.symmetric_difference(m2))
print(max(m))
print(min(m))
print(len(m))
"""

m={1,2,3,44,55,69}
m2={12,13,14,1,2,69}
s1={1,2,3}
s2={4,5,6}

# v=int(input("enter the value"))
m1=m.copy()
print("shalow copy of set is",m1)
print("Ele present in one not in other")
print(m.difference(m2))
print(s1.symmetric_difference(m))
print(s1.isdisjoint(m))
print(s1.isdisjoint(s2))
print(s1.issubset(m))
print(m.issubset(m2))