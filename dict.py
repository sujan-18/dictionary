# practice dictionary from basic
student_details={"name":"sujan","college":"lbef","Degree":"BSCIT","Age":21}
# print(type(student_details))
# print(student_details)

# practice dictionary in another way
student_details1=dict(name="sujan", college="lbef", Degree="BSCIT", Age=21)

# print(student_details["name"])
# print(student_details.get("name"))
x=student_details.keys()
print(x)

student_details["country"]="nepal"
print(x)

y=student_details.values()
print(y)
print("name" not in student_details)
