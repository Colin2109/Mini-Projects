import random
import time
import itertools

zeichen = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

length = int(input("Geben Sie die gewünschte Passwortlänge ein: "))

if length <= 0:
    print("Fehler: Bitte eine gültige positive ganze Zahl eingeben.")
    exit()

def generate_password(length):              # Generiert ein Passwort mit der gegebenen Länge
    password = ""
    for i in range(length):
        password += random.choice(zeichen)
    return password

password = generate_password(length)

print("Generiertes Passwort: ", password)

def bewertung(password):                   # Bewertet das Passwort nach geschätzter Zeit des Brute Force Vorgangs
    charsets = 0

    if any(c.islower() for c in password):
        charsets += 26
    if any(c.isupper() for c in password):
        charsets += 26
    if any(c.isdigit() for c in password):
        charsets += 10
    if any(c in "!@#$%^&*()" for c in password):
        charsets += 10

    kombis = charsets ** len(password)

    # grobe Cracking-Zeit in Sekunden (angenommen 100k Versuche/s)
    attempts_per_sec = 100000
    crack_time_sec = kombis / attempts_per_sec

    if crack_time_sec < 60:
        level = "❌ Sehr unsicher"
    elif crack_time_sec < 3600:
        level = "⚠️ mittelmäßig"
    else:
        level = "✅ stark"

    print("\nBewertung des Passworts:")
    print("Zeichenvorrat:", charsets)
    print("Kombinationen:", kombis)
    print("Geschätzte Cracking-Zeit bei 100k/s:", crack_time_sec, "Sekunden")
    print("Sicherheitslevel:", level)


bewertung(password)

print("Der Vorgang kann bis zu 2 Minuten dauern...")

def brute_force(password, max_time=120):   # Versucht das Passwort mit einer Max Zeit von 2Min zu knacken
    start = time.time()
    attempts = 0

    for length in range(1, len(password) + 1):
        for guess_tuple in itertools.product(zeichen, repeat=length):

            attempts += 1
            guess = ''.join(guess_tuple)

            # Zeitlimit prüfen
            if time.time() - start >= max_time:
                elapsed = time.time() - start
                return None, attempts, elapsed

            if guess == password:
                elapsed = time.time() - start
                return guess, attempts, elapsed

    elapsed = time.time() - start
    return None, attempts, elapsed


found, attempts, total_time = brute_force(password)

if found:
    print(f"Gefunden nach {attempts} Versuchen in {total_time:.4f} Sekunden: {found}")
else:
    print(f"Nicht gefunden nach {attempts} Versuchen in {total_time:.4f} Sekunden.")


