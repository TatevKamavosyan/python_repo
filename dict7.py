person={'name': 'Jessa', 'country': 'USA', 'telephone': 123445, 'weight': 50, 'height': 6}

key_name="country"
if key_name in person.keys():
    print("country name is",person[key_name])
else:
    print("Key not found")