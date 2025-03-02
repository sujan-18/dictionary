my_family={"children1":{"name":"sujan","age":21},"children2":{"name":"sujan1","age":22}} 
# print(my_family)
# print(my_family["children1"]["name"])
# print(my_family["children2"]["age"])
for x,y in my_family.items():
    print(x)
    for z in y:
     print(z +":" , y[z])