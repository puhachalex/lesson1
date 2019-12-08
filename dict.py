mydict = {
    "city":"Москва",
    "temperature": 20
}

print (mydict ["city"])

mydict["temperature"] =  mydict["temperature"]-5

print(mydict)

print(mydict.get("country"))

print(mydict.get("country", "Россия"))

mydict["date"] = "27.05.2019"
print(len(mydict))