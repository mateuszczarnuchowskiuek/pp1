name = "Imię Nazwisko"
university = "Nazwa uniwersytetu"
field = "Kierunek studiów"

file = open("student.txt", "w")

file.write(name+"\n")
file.write(university+"\n")
file.write(field+"\n")

file.close()