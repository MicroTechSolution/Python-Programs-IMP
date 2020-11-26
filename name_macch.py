import re
f = open("output.txt", "r")
content = f.read()
ts = content.split(' ')



'''y = content = filter(lambda x: not re.match(r'^\s*$', x), content)
print(y)'''


'''ts = ["and", "To", "From","Sealey","a","Permanent","Account","fae","INCOME","TAX","Permanent","Number","mec","INCOME","INCOME DEPARTMENT"]
print(' '.join([t for t in ts if not t in ts]))'''

#s = "Python is great and Java is also great"
l = content.split() 
k = []
for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (content.count(i)>1 and (i not in k)or content.count(i)==1): 
        k.append(i)
        

new_list=[]
for e in k:
    if e not in ('1','2','3','4','5','6','7','8','9','0','!','@','$','%','^','&','*','(',')','_','+','=','{','}','[',']',';','"','|','<','>','?','.','/','-','Account','\n','Sealey','fae','a',':','INCOME','TAX','DEPARTMENT','ans','ae','Permanent','Number','mec','nce'):
        new_list.append(e)
k=new_list
stringList=''
stringList = ' '.join([str(item) for item in k ])
k=stringList
print(k)
print("tyt")
