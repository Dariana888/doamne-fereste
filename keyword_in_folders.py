import os

# Cere utilizatorului keyword-ul
keyword = input("Introdu cuvântul cheie de căutat: ")

# Cere utilizatorului folderul de scanat
folder_path = input("Introdu calea către folderul de scanat: ")

# Parcurge folderul și subfolderele
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if keyword in content:
                    print(f"Cuvântul '{keyword}' a fost găsit în: {file_path}")
        except Exception as e:
            # Pentru fișiere binare sau inaccesibile
            pass
          
