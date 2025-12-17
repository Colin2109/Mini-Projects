def Addieren (a , b) :
    return a + b

def Subtrahieren (a , b) :
    return a - b

def Multiplizieren (a , b) :
    return a * b

def Dividieren (a , b) :
    return a / b


a = float(input("Geben Sie die erste Zahl ein: "))
b = float(input("Geben Sie die zweite Zahl ein: "))
zeichen = input(str("Geben Sie das Rechenzeichen ein (+, -, *, /): "))

if zeichen == "+" :
    print("Ergebnis: ", Addieren(a, b))

elif zeichen == "-" :
    print("Ergebnis: ", Subtrahieren(a, b))

elif zeichen == "*" :
    print("Ergebnis: ", Multiplizieren(a, b))

elif zeichen == "/" :
    print("Ergebnis: ", Dividieren(a, b))

else :
    print("Ungültiges Rechenzeichen.")
