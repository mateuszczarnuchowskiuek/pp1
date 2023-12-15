months = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]

def month(n):
    return months[n-1]

print(month(1))
print(month(9))
print(month(12))