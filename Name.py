s1 = 'Roshan chothe p'
s2 = 'p Roshan chothe'
set1 = set(s1.split(' '))
set2 = set(s2.split(' '))
#print(set1 == set2)
if set1 == set2:
    print("Match")
else:
    print("Not match")
