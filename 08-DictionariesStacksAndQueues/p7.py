person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {
        "landline": "1234444321",
        "mobile": "777888999"
    }
}

print(person)

print(person["name"])

print(person["hobby"])

person["surname"] = "Nowak"

person["married"] = not person["married"]

person["gender"] = "male"

person["hobby"].append("bicycle")
print(person["hobby"])

person["phone"]["work"] = "1231354342"

print(person)