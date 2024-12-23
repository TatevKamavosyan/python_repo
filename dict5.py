person_details={"name":"Jessa","country":"USA","telephone":123445}

person_details.setdefault("State","Texas")

person_details.setdefault("zip")
person_details.setdefault("country","Canada")
for key,value in person_details.items():
    print(key,':',value)

