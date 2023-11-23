personal_data = "Mr. John May, born on 1998-02-16"
parsed_data = personal_data.split(",")

title_name_surname = parsed_data[0]
description = personal_data
title, name, surname = title_name_surname.split(" ")
initials = name[0] + surname[0]
born_on_date = parsed_data[1]
empty, born, on, date = born_on_date.split(" ")

print(f"Description: {description}")
print(f"Name: {name}")
print(f"Surname: {surname}")
print(f"Initials: {initials}")
print(f"Born: {date}")