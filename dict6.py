person={'name': 'Jessa', 'country': 'USA', 'telephone': 123445, 'weight': 50, 'height': 6}
deleted_item=person.popitem()
print(deleted_item)

print(person)
deleted_item=person.pop("telephone")

print(person)
del person["weight"]
print(person)
person.clear()
print(person)
del person
print(person)


