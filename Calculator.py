def addieren (a , b) :
    return a + b

def subtrahieren (a , b) :
    return a - b

def multiplizieren (a , b) :
    return a * b

def dividieren (a , b) :
    return a / b


a = float(input("Geben Sie die erste Zahl ein: "))
b = float(input("Geben Sie die zweite Zahl ein: "))
zeichen = input("Geben Sie das Rechenzeichen ein (+, -, *, /): ")

if b == 0 and zeichen == "/" :
    print("Fehler: Division durch Null ist nicht erlaubt.")
    exit()

if zeichen == "+" :
    print("Ergebnis: ", addieren(a, b))

elif zeichen == "-" :
    print("Ergebnis: ", subtrahieren(a, b))

elif zeichen == "*" :
    print("Ergebnis: ", multiplizieren(a, b))

elif zeichen == "/" :
    print("Ergebnis: ", dividieren(a, b))

else :
    print("Ungültiges Rechenzeichen.")

