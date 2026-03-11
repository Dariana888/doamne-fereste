numar = int(input("Introdu o cifra intre 1 si 100: "))

if 1 <= numar <= 100:
    postare = {
        "id": numar,
        "titlu": str(numar)
    }

    print("Postarea a fost creata:")
    print("ID:", postare["id"])
    print("Titlu:", postare["titlu"])
else:
    print("Numarul trebuie sa fie intre 1 si 100!")