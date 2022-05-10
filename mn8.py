import json
a=["neelam","programer","24","2400"]
b=["komal","trainer","24","20000"]
c=["anuradha","HR","25","40000"]
d=["Abhishek","manager","29","63000"]
e=["name","designation","age","salary"]
dict1={}
dict2={}
dict3={}
dict4={}
dict5={}

i=0
while i<len(a):
    dict1[e[i]]=a[i]
    dict2[e[i]]=b[i]
    dict3[e[i]]=c[i]
    dict4[e[i]]=d[i]
    i+=1
dict5["emp1"]=dict1
dict5["emp2"]=dict2
dict5["emp3"]=dict3
dict5["emp4"]=dict4

print(dict5)