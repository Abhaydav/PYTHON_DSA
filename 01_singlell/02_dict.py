dic1={
    'value':11
}

dic2=dic1
print(dic1)
print(dic2)

print(id(dic1))
print(id(dic2))


dic2['value']=22
print(dic1)
print(dic2)

print(id(dic1))
print(id(dic2))

