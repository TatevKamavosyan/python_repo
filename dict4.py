person={"name":"Jessa","country":"USA","telephone":123445}



person["weight"]=50
person.update({"height":6})
person.update({"age":20,"gender":"famile"})
print(person)
print(type(person))
person.update([("city","Orlando"),("Company","Google")])
print(person)
print("There are",len(person),"items in dictonary")