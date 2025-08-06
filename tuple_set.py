#TUPLE
s = (34,34,65,36,7,8)
print(s)
print(type(s))
#TYPECASTIN
s = (34,34,65,36,7,8)
m = list(s)
m[4]=4
s = tuple(m)
print(s)

# MUL
m = (3,4)
c =m*3
print(c)

#UNPACKING
s = ("aplle","annna","this")
(green,tt,d)=s
print(green)


"""this is set """
#SET IN PYTHON
se = {1,2,4,6,7,3,3,2}
print(se)
print(type(se))

#ADD IN SET
se ={23,53,3,5}
se.add(43)
print(se)

#INTERSECTION
se = {3,3,5,7,57}
m ={3,6,46,75,2,5}
c = se.intersection(m)
print(c)

#UNION
se = {3,3,5,7,57}
m ={3,6,46,75,2,5}
c = se.union(m)
print(c)

#DIFFERENCE
se = {3,3,5,7,57}
m ={3,6,46,75,2,5}
c = se.difference(m)
print(c)

#REMOVE IN SET
se = {1,2,4,6,7,3,3,2}
se.remove(2)
print(se)

#COPY IN SET
se = {1,2,4,6,7,3,3,2}
m = se.copy()
print(m)

#APPEND IN SET
se = {1,2,4,6,7,3,3,2}
se.add("tis")
print(se)
